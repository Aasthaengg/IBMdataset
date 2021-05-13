from collections import deque

n = int(input())
A = list(map(int, input().split()))

A.sort()
A_d = deque(A)

if (A_d[0] <= 0 and A_d[n-1] > 0) or (A_d[0] < 0 and A_d[n-1] >= 0):
    print(sum(list(map(abs, A_d))))
    while A_d[-2] >= 0:
        atama = A_d.popleft()
        ketu = A_d.pop()
        print(atama, ketu)
        new = atama - ketu
        A_d.appendleft(new)
    while len(A_d) != 1:
        atama = A_d.popleft()
        ketu = A_d.pop()
        print(ketu, atama)
        new = ketu - atama
        A_d.append(new)
elif A_d[0] > 0:
    atama = A_d.popleft()
    tugi = A_d.popleft()
    new = atama - tugi
    A_d.appendleft(new)
    print(sum(list(map(abs, A_d))))
    print(atama, tugi)
    while len(A_d) != 2:
        atama = A_d.popleft()
        ketu = A_d.pop()
        print(atama, ketu)
        new = atama - ketu
        A_d.appendleft(new)
    atama = A_d.popleft()
    ketu = A_d.pop()
    print(ketu, atama)
else:
    ketu = A_d.pop()
    tugi = A_d.pop()
    new = ketu - tugi
    A_d.append(new)
    print(sum(list(map(abs, A_d))))
    print(ketu, tugi)
    while len(A_d) != 1:
        atama = A_d.popleft()
        ketu = A_d.pop()
        print(ketu, atama)
        new = ketu - atama
        A_d.append(new)