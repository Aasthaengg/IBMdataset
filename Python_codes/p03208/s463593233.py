n, k = map(int, input().split())
trees = [int(input()) for _ in range(n)]
trees.sort()
diff_trees_height = []

for i in range(n - (k - 1)):
    diff = abs(trees[i] - trees[i + k - 1])
    diff_trees_height.append(diff)
print(min(diff_trees_height))
