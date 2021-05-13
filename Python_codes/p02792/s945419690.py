import sys
N = int(sys.stdin.readline().rstrip())

cnt = [[0] * 10 for _ in range(10)]

for i in range(1, N + 1):
    i = str(i)
    cnt[int(i[0])][int(i[-1])] += 1

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += cnt[i][j] * cnt[j][i]
print(ans)