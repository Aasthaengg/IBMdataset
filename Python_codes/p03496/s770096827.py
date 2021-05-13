N = int(input())
a = list(map(int,input().split()))

m = 10**6+1
M = -10**6-1
j = -1
k = -1
for i in range(N):
    if M < a[i]:
        M = a[i]
        j = i
    if m > a[i]:
        m = a[i]
        k = i

print(2*N-2)
if -m < M:
    for i in range(N):
        if i != j:
            print('{} {}'.format(j+1,i+1))
    for i in range(N-1):
        print('{} {}'.format(i+1,i+2))
else:
    for i in range(N):
        if i != k:
            print('{} {}'.format(k+1,i+1))
    for i in range(N-1,0,-1):
        print('{} {}'.format(i+1,i))