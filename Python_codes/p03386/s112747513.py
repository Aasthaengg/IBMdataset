A, B, K = map(int, input().split())
res = set()
for i in range(K):
    if A + i <= B:
        res.add(A + i)
    if B - i >= A:
        res.add(B - i)
res = sorted(list(res))
print(*res, sep='\n')