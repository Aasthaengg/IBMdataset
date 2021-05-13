N = int(input())
P = [int(input()) for _ in range(N)]

V = [-1] * (N+1)
for i in range(N):
    V[P[i]] = i+1
# print(V)

c = 0
ans = 0
for i in range(1, N+1):
    if V[i-1] > V[i]:
        c = 1
    else:
        c += 1
    ans = max(c, ans)

print(N-ans)
