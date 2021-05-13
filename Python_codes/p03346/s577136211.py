N = int(input())
P = [int(input()) for i in range(N)]
Q = {}
for i in range(N):
    Q[P[i]] = i

tmp = 1
ans = 1
for i in range(1, N):
    if Q[i] < Q[i + 1]:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 1
ans = max(ans, tmp)
print(N - ans)