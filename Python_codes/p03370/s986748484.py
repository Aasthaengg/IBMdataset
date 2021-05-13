n , x = map(int,input().split())
m = [int(input()) for _ in range(n)]

#n,x = 3,1000
#m = [120, 100, 140]

x = x - sum(m)
minm = min(m)

ans = len(m) + int(x/minm)

print(ans)