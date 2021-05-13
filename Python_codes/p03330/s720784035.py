from itertools import permutations

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
X = [list(map(int, input().split())) for _ in range(N)]

memo = [[0] * C for _ in range(3)]
for i in range(N):
    for j in range(N):
        k = (i + j + 2) % 3
        memo[k][X[i][j] - 1] += 1
        
ans = 10 ** 9 + 7
for c in permutations(range(C), 3):
    cost = 0
    for n in range(3):
        for j in range(C):
            cost += D[j][c[n]] * memo[n][j]
            
    ans = min(ans, cost)
    
print(ans)
