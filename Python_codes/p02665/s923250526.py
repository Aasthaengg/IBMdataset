n = int(input())
leaves = list(map(int, input().split()))

sum_leaves = [0]*(n+1)
sum_leaves[0] = leaves[0]
for depth in range(n):
    sum_leaves[depth+1] = sum_leaves[depth] + leaves[depth+1]

ans = 0

root = [None] * (n + 1)
if n == 0:
    root[0] = 0
else:
    root[0] = 1
if root[0] + leaves[0] != 1:
    print(-1)
else:
    for depth in range(n):
        root[depth+1] = min(2*root[depth]-leaves[depth+1],
                            sum_leaves[n]-sum_leaves[depth+1])
        if root[depth + 1] < root[depth] - leaves[depth + 1] or root[depth+1] < 0:
            print(-1)
            break
    else:
        print(sum(root)+sum(leaves))
