A, B, K = map(int, input().split())
ans = []
for i in range(A, min(A+K, B+1)):
    ans += [i]
for i in range(max(A, B-K+1), B+1):
    ans += [i]

ans = list(set(ans))
ans = sorted(ans)
for a in ans:
    print(a)