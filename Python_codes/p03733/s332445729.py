n, t = map(int, input().split())
T = list(map(int, input().split()))

ans = 0
temp = 0
for i in range(n):
    ans += min(t, T[i]-temp)
    temp = T[i]
else:
    ans += t
print(ans)
