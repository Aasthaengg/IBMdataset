N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
m = -10*100
for i in range(2**N):
    tmp = 0
    for j in range(N):
        if (i>>j)&1:
            tmp += V[j]-C[j]
    m = max(tmp, m)

print(m)