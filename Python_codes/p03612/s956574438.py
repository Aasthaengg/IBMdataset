N = int(input())
P = [int(_) for _ in input().split()]
cnt = 0

for i in range(N):
    p = P[i]
    ni = (i + 1) % N
    if p == (i + 1):
        cnt += 1
        P[i], P[ni] = P[ni], P[i]

print(cnt)
