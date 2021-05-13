N = int(input())
v = list(map(int, input().split()))
v.sort(reverse=True)
ans = 0
x = 2
for i in range(N):
    if i == N - 1:
        x /= 2
    ans += v[i] / x
    x *= 2
print(ans)
