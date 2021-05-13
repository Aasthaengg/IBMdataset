N = int(input())

dp_table = [[0] * N for j in range(3)]

a, b, c = map(int, input().split())
dp_table[0][0] = a
dp_table[1][0] = b
dp_table[2][0] = c

for i in range(1, N):
    a, b, c = map(int, input().split())
    dp_table[0][i] = max(dp_table[1][i-1] + a, dp_table[2][i-1] + a)
    dp_table[1][i] = max(dp_table[0][i-1] + b, dp_table[2][i-1] + b)
    dp_table[2][i] = max(dp_table[0][i-1] + c, dp_table[1][i-1] + c)

print(max(dp_table[0][N-1], dp_table[1][N-1], dp_table[2][N-1]))
