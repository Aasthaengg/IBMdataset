#実験用の写経
N = int(input())
g = {i: [] for i in range(N)}
for i in range(N - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
c = list(map(int, input().split()))
c.sort()
print(sum(c[:-1]))
nums = [0] * N
stack = [0]
while stack:
    d = stack.pop()
    nums[d] = c.pop()
    for node in g[d]:
        if nums[node] == 0:
            stack.append(node)
print(' '.join(map(str, nums)))
