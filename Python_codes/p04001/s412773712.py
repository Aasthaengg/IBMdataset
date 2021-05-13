# C - たくさんの数式
s = list(input())
n = len(s)
a = 0
for i in range(2 ** (n-1)):
    l = []
    l.append(s[0])
    for j in range(n-1):
        if (i & 1 << j):
            l.append('+')
        l.append(s[j+1])
    a += eval(''.join(l))

print(a)

