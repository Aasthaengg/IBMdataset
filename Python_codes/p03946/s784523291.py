N, T = map(int, input().split())
A = list(map(int, input().split()))

m = A[0]
l = []
for i in range(1, N):
    if A[i] < m:
        m = A[i]
    else:
        d = A[i] - m
        l.append(d)
print(l.count(max(l)))