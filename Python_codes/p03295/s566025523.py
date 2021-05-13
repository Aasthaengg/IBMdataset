N, M = map(int, input().split())
T = []
for i in range(M):
    a, b = map(int, input().split())
    T.append([a, b])

T.sort()
c = 1
s = 1
e = 10**9
for i in range(M):
    a = T[i][0]
    b = T[i][1]
    if a >= e and b > e:
        c += 1
        s = a
        e = b
    elif a > s and b < e:
        s = a
        e = b
    elif a > s:
        s = a
    elif b < e:
        e = b
    else:
        pass
print(c)