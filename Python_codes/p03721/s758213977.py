n,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

a = sorted(a,key=lambda x:x[0])
ans = 0
for i in range(n):
    ans += a[i][1]
    if ans >= k:
        print(a[i][0])
        exit()