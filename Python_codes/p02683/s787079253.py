import numpy as np
N,M,X = map(int,input().split())
C = np.repeat(0, N)
A = np.repeat(0, N*M).reshape(N,M)
for i in range(N):
    x = list(map(int, input().split()))
    C[i] = x[0]
    A[i,:] = x[1:]

ans = np.inf

for _ in range(1<<N):
    # print(format(_, 'b').zfill(H+W))
    choices = [i for i,v in enumerate(format(_, 'b').zfill(N)) if v == '1']
    points = A[choices,:].sum(axis=0)
    if sum(points < X) == 0:
        ans = min(ans, sum(C[choices]))

ans = [ans, -1][np.isinf(ans)]
print(ans)