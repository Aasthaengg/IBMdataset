N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
A = [V[i]-C[i] for i in range(N)]
cnt = 0
for i in range(N):
    if A[i]>0:
        cnt += A[i]
print(cnt)