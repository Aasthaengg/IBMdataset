N, C = map(int, input().split())
R = 10**5
T = [[0] * (R+1) for _ in range(C)]
for _ in range(N):
    s, t, c = map(int, input().split())
    T[c-1][s] += 1
    T[c-1][t] -= 1

A = [0] * (R+1)
ans = 0
for i in range(R):
    for c in range(C):
        A[i] += T[c][i+1] if T[c][i+1] > 0 else 0
        A[i] += T[c][i] if T[c][i] < 0 else 0
    A[i+1] += A[i]
    ans = max(ans, A[i+1])
print(ans)
