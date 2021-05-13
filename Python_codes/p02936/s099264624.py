import sys
sys.setrecursionlimit(1000000)

n, q = map(int, input().split())
tree = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    tree[a].append(b)
    tree[b].append(a)

ans = [0 for _ in range(n)]

for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x

checked = [False] * n
checked[0] = True


def function(now, count):
    ans[now] += count
    for i in tree[now]:
        if checked[i] == False:
            checked[i] = True
            function(i, ans[now])

function(0, 0)

for a in ans:
    print(a)