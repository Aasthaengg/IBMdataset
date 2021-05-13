n, k = map(int, input().split())
tree = [int(input()) for _ in range(n)]
tree.sort()
ans = 10 ** 9 + 7

for i in range(k-1, n):
    ans = min(ans, tree[i] - tree[i-k+1])

print(ans)