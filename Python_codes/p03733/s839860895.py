N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
t.append(t[-1] + 2 * T)

for i in range(N):
    ans += min(T, t[i + 1] - t[i])

print (ans)