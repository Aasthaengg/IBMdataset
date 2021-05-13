N = int(input())
a = [input().split() for i in range(2)]
candy = [int(a[i][j]) for i in range(2) for j in range(N)]
MAX = 0

for i in range(N):
    MAX = max(MAX, sum(candy[:i+1]) + sum(candy[i+N:]))

print(MAX)