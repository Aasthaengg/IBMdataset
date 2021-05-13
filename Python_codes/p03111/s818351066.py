N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
def dfs(i, a, b, c):
    if i == N:
        if a == 0 or b == 0 or c == 0:
            return float('inf')
        else:
            return abs(A-a)+abs(B-b)+abs(C-c)-30
    four = dfs(i+1, a, b, c)
    one = dfs(i+1, a+l[i], b, c) + 10
    two = dfs(i+1, a, b+l[i], c) + 10
    three = dfs(i+1, a, b, c+l[i]) + 10
    return min(one, two, three, four)
print(dfs(0, 0, 0, 0))