N = int(input())
*A, = map(int, input().split())
operations = []
pos = []; zero = []; neg = [];
for a in A:
    if a > 0: pos.append(a)
    elif a == 0: zero.append(a)
    else: neg.append(a)
pos.sort(); neg.sort()
if N == 2:
    a, b = max(A), min(A)
    ans = a - b
    operations.append((a, b))
else:
    if len(neg) == 0:
        pos = zero + pos
        operations.append((pos[0], pos[-1]))
        neg = [pos[0] - pos[-1]]
        pos = pos[1:-1]
    elif len(pos) == 0:
        neg = neg + zero
        operations.append((neg[-1], neg[0]))
        pos = [neg[-1] - neg[0]]
        neg = neg[1:-1]
    else:
        neg = neg + zero
    neg = neg[::-1]
    while len(pos) > 1 and len(neg) > 1:
        n, p = neg.pop(), pos.pop()
        operations.append((p, n))
        pos.append(p-n)
    if len(neg) == 1:
        while len(pos) > 1:
            n, p = neg.pop(), pos.pop()
            operations.append((n, p))
            neg.append(n-p)
    else:
        while len(neg) > 1:
            n, p = neg.pop(), pos.pop()
            operations.append((p, n))
            pos.append(p-n)
    operations.append((pos[0], neg[0]))
    ans = pos[0] - neg[0]
print(ans)
for x, y in operations:
    print(x, y)