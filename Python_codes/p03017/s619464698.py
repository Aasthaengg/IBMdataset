from itertools import groupby
n, a, b, c, d = map(int, input().split())
s = input()

g = groupby(s[a:c])
h = groupby(s[b:d])

for i, j in g:
    if i == "#" and len(list(j)) > 1:
        print("No")
        exit()

for i, j in h:
    if i == "#" and len(list(j)) > 1:
        print("No")
        exit()

if c < d:
    print("Yes")
    exit()

e = groupby(s[b-2:d+1])
for i, j in e:
    if i == "." and len(list(j)) > 2:
        print("Yes")
        exit()

print("No")