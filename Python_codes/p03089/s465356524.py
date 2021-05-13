n = int(input())
b = [int(i) for i in input().split()]
s = []

while len(b) > 0:
    m = -1
    for i in range(len(b)):
        if b[i] == i + 1:
            m = i
    if m == -1:
        break
    else:
        s.append(b.pop(m))

if m == -1:
    print(-1)
else:
    print(*reversed(s), sep='\n')