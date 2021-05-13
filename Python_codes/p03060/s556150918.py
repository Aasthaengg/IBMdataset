N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
total = 0
for n in range(N):
    if V[n]-C[n] > 0:
        total += V[n]-C[n]
print(total)