L, R, d = map(int, input().split())
ans = 0
for i in range(d, R+1, +d):
    ans += i >= L
print(ans)
