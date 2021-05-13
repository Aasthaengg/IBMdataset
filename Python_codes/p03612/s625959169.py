import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

ans = 0
for i, p_i in enumerate(P):
    if p_i == i + 1:
        if i + 1 == N:
            P[i], P[i-1] = P[i-1], P[i]
        else:
            P[i+1], P[i] = P[i], P[i+1]
        ans += 1

print(ans)