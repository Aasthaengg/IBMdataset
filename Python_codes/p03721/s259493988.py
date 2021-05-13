n,k = map(int,input().split())
L = []
for i in range(n):
    a,b = map(int,input().split())
    L.append([a,b])
L.sort()
ans = 0
sum1 = 0
for i in range(n):
    sum1 +=L[i][1]
    ans = L[i][0]
    if sum1 >=k:
        print(ans)
        exit()
