N, M, Q = map(int, input().split())

def make_group(now, n, i):
    if n == 0:
        groups.append(now)
    else:
        for j in range(i, M+1): 
            make_group(now+[j], n-1, j)

A = [0]*Q
B = [0]*Q
C = [0]*Q
D = [0]*Q
for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())

groups = []
now = []
make_group(now, N, 1)

ans = 0
for group in groups:
    tmp = 0
    for a, b, c, d in zip(A, B, C, D):
        if group[b-1]-group[a-1] == c:
            tmp += d
    ans = max(ans, tmp)
print(ans)
