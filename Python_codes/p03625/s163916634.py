N = int(input())
A = list(map(int, input().split()))

A.sort(key=lambda x: -x)

l = []

a_old = -1
for a in A:
    if a_old == a:
        l.append(a)
        a_old = -1
    else:
        a_old = a

l.append(0)
l.append(0)

print(l[0] * l[1])