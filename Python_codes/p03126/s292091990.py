N, M = map(int, input().split())
ans = [0 for _ in range(M)]
for i in range(N):
    a = list(map(int, input().split()))
    for i in a[1:]:
        ans[i-1] += 1
print(ans.count(N))
