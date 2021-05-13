import sys
sys.setrecursionlimit(10**7)

n, m = [int(i) for i in sys.stdin.readline().split()]
parent = [i for i in range(n)]

graph = {j:[] for j in range(n)}
for i in range(m):
    l, r, d = [int(i) for i in sys.stdin.readline().split()]
    l -= 1
    r -= 1
    graph[l].append((r, d))
    graph[r].append((l, -d))

already = set()
x_ls = [None for i in range(n)]
x_ls[0] = 0
stack = list(range(n))[::-1]
flg = True
while len(stack) > 0:
    cur = stack.pop(-1)
    if cur in already:
        continue
    if x_ls[cur] is None:
        cur_pos = 0
    else:
        cur_pos = x_ls[cur]
    already.add(cur)
    for _next, dis in graph[cur]:
        if x_ls[_next] is None:
            x_ls[_next] = cur_pos + dis
            stack.append(_next)
        else:
            if x_ls[_next] != cur_pos + dis:
                flg = False
                break
    if not flg:
        break
if flg:
    print("Yes")
else:
    print("No")