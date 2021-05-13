h, w = map(int, input().split())
lst = []
block = 0
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == '#':
            block += 1
        lst.append(s[j])
queue = [(1, 0)]
visited = set()
flag = False
while queue:
    #print(queue)
    step, pos = queue.pop(0)
    if pos in visited:
        continue
    if pos == h * w - 1:
        flag = True
        ans = step
        break
    visited.add(pos)
    step += 1
    if pos > (pos // w) * w:
        if lst[pos - 1] == '.':
            queue.append((step, pos - 1))
    if pos < ((pos // w) + 1) * w - 1:
        if lst[pos + 1] == '.':
            queue.append((step, pos + 1))
    if pos >= w:
        if lst[pos - w] == '.':
            queue.append((step, pos - w))
    if pos < (h - 1) * w:
        if lst[pos + w] == '.':
            queue.append((step, pos + w))
if flag:
    print(h * w - block - ans)
else:
    print(-1)