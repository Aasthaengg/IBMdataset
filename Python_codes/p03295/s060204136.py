n, m = map(int, input().split())
events = []
for i in range(m):
    a, b = map(int, input().split())
    events.append((a, 0, i))
    events.append((b-1, 1, i))
events.sort()
solved = [False] * m
todo = []
ans = 0
for i, etype, req in events:
    if etype == 0:
        todo.append(req)
    else:
        if not solved[req]:
            ans += 1
            for req_id in todo:
                solved[req_id] = True
            todo = []
print(ans)