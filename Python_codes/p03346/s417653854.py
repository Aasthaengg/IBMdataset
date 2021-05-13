N = int(input())
p = [int(input()) for _ in range(N)]
q = [0] * N
for i in range(N):
    q[p[i] - 1] = i
cnt = 0
ma = 0
for i in range(N - 1):
    if q[i] < q[i + 1]:
        cnt += 1
        ma = max(ma, cnt)
    else:
        cnt = 0
print(N - 1 - ma)