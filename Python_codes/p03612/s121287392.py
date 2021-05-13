N = int(input())
P = list(map(int, input().split()))

res = 0
for i in range(N-1):
    if P[i] == i+1:
        P[i+1] = i+1
        res += 1
if P[-1] == N:
    res += 1

print(res)