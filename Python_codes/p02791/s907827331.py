N = int(input())
P = [int(p) for p in input().split()]

M = N+1
cnt = 0
for p in P:
    if p < M:
        cnt += 1
        M = p

print(cnt)