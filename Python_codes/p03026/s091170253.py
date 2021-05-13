N = int(input())
edges = [list(map(int, input().split())) for i in range(N-1)]
c = list(map(int, input().split()))
c.sort(reverse=True)
_c = c[::]

conn = [[] for i in range(N)]
for edge in edges:
    a = edge[0]-1
    b = edge[1]-1
    conn[a].append(b)
    conn[b].append(a)
ans = [0 for i in range(N)]
stack = []
stack.append(0)
checked = set()
while len(stack) > 0:
    current = stack.pop(0)
    checked.add(current)
    ans[current] = c[0]
    c.pop(0)
    for next in conn[current]:
        if next not in checked:
            stack.append(next)

print(sum(_c[1:]))
ans_str = ""
for i in range(N):
    ans_str += str(ans[i])
    if i < N-1:
        ans_str += " "
print(ans_str)





