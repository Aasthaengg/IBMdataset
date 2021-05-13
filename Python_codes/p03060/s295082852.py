N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
D = []
res = 0
for i in range(N):
    t = V[i] - C[i]
    if t>0:
        res += t
print(res)