N = int(input())
H = list(map(int, input().split()))
height_memo = [float('inf')] * N
height_memo[0] = 0
height_memo[1] = abs(H[1] - H[0])

for i in range(N - 2):
    height_memo[i + 2] = min(height_memo[i] + abs(H[i + 2] - H[i]),
                             height_memo[i + 1] + abs(H[i + 2] - H[i + 1]))

print(height_memo[N - 1])