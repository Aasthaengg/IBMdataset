N,M = map(int,input().split())
C = [0] * (M+1)
for i in range(N):
    K = list(map(int, input().split()))
    for k in range(len(K)):
        if k != 0:
            C[K[k]] += 1
count = 0

for c in C:
    if c == N:
        count += 1

print(count)