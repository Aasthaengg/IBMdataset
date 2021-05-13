import sys
input = sys.stdin.readline

N = int(input())
edge = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)


def dist(root):  # 根をnとしたときの各点の深さ
    res = [-1] * (N + 1)
    node = [root]
    res[root] = 0
    while node:
        s = node.pop()
        d = res[s]
        for t in edge[s]:
            if res[t] == -1:
                node.append(t)
                res[t] = d + 1
    return res[1:]


fenek = dist(1)
snuke = dist(N)
f, s = 0, 0
for i, j in zip(fenek, snuke):
    if i <= j:
        f += 1
    else:
        s += 1

ans = "Fennec" if f > s else "Snuke"
print(ans)
