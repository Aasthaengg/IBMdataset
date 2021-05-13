N = int(input())

def f(k):
    s = str(k)
    n = len(s)
    ans = 0
    for i in range(n):
        ans += int(s[i])
    return ans

ans = float("INF")
for i in range(1, N):
    j = N-i
    t = f(i) + f(j)
    ans = min(ans, t)

print(ans)