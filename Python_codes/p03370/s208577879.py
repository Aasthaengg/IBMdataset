n , x = map(int,input().split())
mi = 10**9
ans = 0
for i in range(n):
    now = int(input())
    ans += 1
    x -= now
    mi = min(mi,now)
ans += x//mi
print(ans)