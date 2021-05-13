A, B, K = map(int, input().split())
ans = set()
arr = range(A, B+1)
for a in arr[:K]:
    ans.add(a)
for a in arr[-K:]:
    ans.add(a)

ans = list(ans)
ans.sort()

for a in ans:
    print(a)