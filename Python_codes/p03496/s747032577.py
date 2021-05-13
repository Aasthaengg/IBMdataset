
N = int(input())

a = list(map(int,input().split()))

lis = []


mi = float("inf")
ma = float("-inf")
mi_ind = 0
ma_ind = 0

for i in range(N):

    if mi > a[i]:
        mi = a[i]
        mi_ind = i
    if ma < a[i]:
        ma = a[i]
        ma_ind = i
        
flag = None
if mi < 0 and 0 < ma:

    if abs(mi) <= abs(ma):

        flag = 0

        for i in range(N):

            if a[i] < 0:
                lis.append([ma_ind + 1,i+1])

    else:

        flag = 1

        for i in range(N):

            if a[i] > 0:
                lis.append([mi_ind + 1,i+1])

if mi >= 0 or flag == 0:

    for i in range(N-1):

        lis.append([i+1,i+2])

else:

    for i in range(N-1):

        lis.append([N-i,N-1-i])


print (len(lis))

for i in lis:

    print (i[0],i[1])
    
