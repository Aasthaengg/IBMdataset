N, C = map(int, input().split())
X, V = [], []
for i in range(N):
    x, v = map(int, input().split())
    X.append(x)
    V.append(v)

st1 = [0] * N
st2 = [0] * N
st1[0] = max(0, V[0] - X[0])
st2[0] = max(0, V[0] - 2 * X[0])
cur1, cur2 = V[0] - X[0], V[0] - 2 * X[0]
pre = X[0]
for i in range(1, N):
    cur1 += V[i] - (X[i] - pre)
    cur2 += V[i] - (X[i] - pre) * 2
    st1[i] = max(st1[i - 1], cur1)
    st2[i] = max(st2[i - 1], cur2)
    pre = X[i]

ba1 = [0] * N
ba2 = [0] * N
ba1[-1] = max(0, V[-1] - (C - X[-1]))
ba2[-1] = max(0, V[-1] - 2 * (C - X[-1]))
cur1, cur2 = V[-1] - (C - X[-1]), V[-1] - 2 * (C - X[-1])
pre = X[-1]
for i in range(N - 2, -1, -1):
    cur1 += V[i] - (pre - X[i])
    cur2 += V[i] - (pre - X[i]) * 2
    ba1[i] = max(ba1[i + 1], cur1)
    ba2[i] = max(ba2[i + 1], cur2)
    pre = X[i]

num = 0
num = max(st1[N - 1], ba1[0])
for i in range(N - 1):
    num = max(num, st1[i] + ba2[i + 1])

for i in range(1, N - 1):
    num = max(num, ba1[i] + st2[i - 1])

print(num)