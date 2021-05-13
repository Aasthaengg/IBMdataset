N = int(input())

V = list(input().split())
V = [int(V[i]) for i in range(N)]

C = list(input().split())
C = [int(C[i]) for i in range(N)]

Ans = 0

for i in range(N):
    if V[i] - C[i] >= 0:
        Ans += V[i] - C[i]
        
print(Ans)