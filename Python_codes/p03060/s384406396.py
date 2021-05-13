from itertools import product as p

N = int(input())
*V, = map(int, input().split())
*C, = map(int, input().split())

ans = -10**12
for i in p(range(2), repeat=N):
    X, Y = 0, 0
    for j, k in enumerate(i):
        if k==1:
            X += V[j]
            Y += C[j]
    ans = max(ans, X-Y)
print(ans)