import itertools
a, b, c = map(int, input().split())
V = itertools.permutations([a, b, c])
s = a+b+c
for v in V:
    S = abs(v[1]-v[0])+abs(v[2]-v[1])
    if S < s:
        s = S
print(s)