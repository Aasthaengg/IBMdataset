N, T = map(int, input().split())

t = list(map(int, input().split()))
diff = []

for i in range(1, N):
    diff.append(t[i]-t[i-1])
diff.append(T)

ans = 0
for d in diff:
    ans += min(T, d)
print(ans)
