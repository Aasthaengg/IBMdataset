N = int(input())
H = list(map(int, input().split()))
table = [0 for _ in range(N)]
max_moves = 0

for i in range(-2, -N-1, -1):
    if H[i] >= H[i+1]:
        table[i] = table[i+1] + 1
        max_moves = max(table[i], max_moves)

print(max_moves)
