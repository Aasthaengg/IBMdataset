
def Com(n, k):
    p, q = 1, 1
    for i in range(n-k+1, n+1):
        p *= i
    for i in range(2, k+1):
        q *= i
    return p//q

N = int(input())
print(Com(N, 2)-N//2)
if N & 1:
    for i in range(1, N):
        for j in range(i+1, N+1):
            if i+j != N:
                print(i, j)
else:
    for i in range(1, N):
        for j in range(i+1, N+1):
            if i+j != N+1:
                print(i, j)
