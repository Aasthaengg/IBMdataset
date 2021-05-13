# ABC057_B
N, M = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
checkpoints = [list(map(int, input().split())) for _ in range(M)]

def manhattan(x1,y1,x2,y2):
    res = abs(x1-x2) + abs(y1-y2)
    return res

for i in range(N):
    memo = [float("inf")]*M
    for j in range(M):
        memo[j] = manhattan(*students[i],*checkpoints[j])
    ans = memo.index(min(memo)) + 1
    print(ans)
