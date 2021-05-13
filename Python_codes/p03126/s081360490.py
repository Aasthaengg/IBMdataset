N, M = map(int, input().split())
res = set(list(range(1, M+1)))
for _ in range(N):
    k, *a = map(int, input().split())
    res = res.intersection(a)
print(len(res))