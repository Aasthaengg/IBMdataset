n, m = map(int, input().split())
ans = [0] * m
for i in range(n):
    a = list(map(int, input().split()))
    k = a.pop(0)
    for j in range(k):
        ans[a[j] - 1] += 1
print(ans.count(n))
