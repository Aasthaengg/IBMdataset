N, T = map(int, input().split())
t = list(map(int, input().split()))
lastOn = t[0]
ans = 0
for i in range(1,N):
    ti = t[i]
    ans += min(T, ti-lastOn)
    lastOn = ti
ans += T
print(ans)
