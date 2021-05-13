n = int(input())
b = list(map(int, input().split()))
fl = [False] * n
q = []
while len(b) != 0:
    ptr = -1
    for i in range(len(b)):
        if b[i] == i+1:
            ptr = i

    if ptr == -1:
        break

    _b = []
    for i in range(len(b)):
        if i == ptr:
            q.append(b[i])
        else:
            _b.append(b[i])

    b = _b.copy()

if ptr == -1:
    print(ptr)
else:
    for qq in reversed(q):
        print(qq)
