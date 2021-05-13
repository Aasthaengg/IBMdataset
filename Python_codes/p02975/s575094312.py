n = int(input())

a = list(map(int,input().split()))
a.sort()
d = {}
for i in range(n):
    if(a[i] not in d):d[a[i]] = 1
    else:d[a[i]] += 1
if(len(d) == 1):
    if(a[0] == 0):
        print('Yes')
        exit()
elif(n%3 == 0):
    if(len(d) == 2):
        if(0 in d):
            if(d[0] == n // 3):
                print('Yes')
                exit()
    elif(len(d) == 3):
        k = list(d.keys())
        if(k[0]^k[1]^k[2] == 0):
            if(d[k[0]] == n // 3 and d[k[1]] == n // 3 and d[k[2]] == n // 3):
                print('Yes')
                exit()
print('No')