N, A, B, C = map(int, input().split())

L = [int(input()) for _ in range(N)]

ans = []
def dfs(idx, a, b, c, mp10):
    if idx==N:
        if a and b and c:
            ans.append(abs(A-a)+abs(B-b)+abs(C-c)+mp10*10)
    else:
        dfs(idx+1, a, b, c, mp10)
        dfs(idx+1, a+L[idx], b, c, mp10+1)
        dfs(idx+1, a, b+L[idx], c, mp10+1)
        dfs(idx+1, a, b, c+L[idx], mp10+1)

dfs(0, 0, 0, 0, -3)

print(min(ans))