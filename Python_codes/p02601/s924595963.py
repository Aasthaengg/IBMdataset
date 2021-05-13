A, B, C = map(int, input().split())
K = int(input())


def dfs(a, b, c, k):
    # print(a, b, c, k)
    yield (a, b, c)
    if k+1 <= K:
        for x, y, z in dfs(a, b*2, c, k+1):
            yield (x, y, z)
        for x, y, z in dfs(a, b, c*2, k+1):
            yield (x, y, z)


for a, b, c in dfs(A, B, C, 0):
    if a < b < c:
        print('Yes')
        exit()
print('No')
