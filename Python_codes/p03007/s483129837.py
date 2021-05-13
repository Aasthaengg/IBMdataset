n = int(input())
A = map(int, input().split())

pos = []
neg = []
for a in A:
    if 0 <= a:
        pos.append(a)
    else:
        neg.append(a)


ans = []
if pos:
    if not neg:
        pos.sort(reverse=True)
        neg.append(pos.pop())

    while len(pos) != 1:
        x = pos.pop()
        ans.append((neg[-1], x))
        neg[-1] -= x
else:
    neg.sort()
    pos.append(neg.pop())

pos = pos[0]
while neg:
    x = neg.pop()
    ans.append((pos, x))
    pos -= x

print(pos)
for row in ans:
    print(*row)