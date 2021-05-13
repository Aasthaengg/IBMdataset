N = int(input())
P = list(map(int, input().split()))

cnt = 0
m = 2 * 10 ** 5 + 1
for i in range(N):
    if P[i] <= m:
        m = P[i]
        cnt += 1
print(cnt)
