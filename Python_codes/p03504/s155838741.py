import sys
input = sys.stdin.readline


n, c = map(int, input().split())

TABLE = [[0] * 10**5 for _ in range(c)]
for _ in range(n):
    s, t, i = [int(x) - 1 for x in input().split()]
    for j in range(s, t + 1):
        TABLE[i][j] = 1

answer = 0
for j in range(10**5):
    temporary = sum(TABLE[i][j] for i in range(c))
    answer = max(answer, temporary)

print(answer)
