# -*- coding: utf-8 -*-
N = int(input())

a, b, c, d = 0, 0, 0, 0
for _ in range(N):
    s = input()
    if s.startswith('B') and s.endswith('A'):
        a += 1
    elif s.startswith('B'):
        b += 1
    elif s.endswith('A'):
        c += 1

    d += s.count('AB')

# print(a, b, c, d)

if a == 0:
    print(d + min(b, c))

elif b == 0 and c == 0:
    print(d + a -1 )

else:
    print(d + a + min(b, c))