N, M = map(int, input().split())
d = [0]*M
for _ in range(N):
    K, *A = map(int, input().split())
    for a in A:
        d[a-1] += 1
print(d.count(N))