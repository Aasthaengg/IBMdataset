n, k, c = map(int, input().split())
s = input()
fo = []
ba = []
r = 0
for ind, cc in enumerate(s):
    ind += 1
    r -= 1
    if cc=='x' or r>0:
        continue
    fo.append(ind)
    if len(fo)==k:
        break
    r = c+1
r = 0
for ind, cc in enumerate(reversed(s)):
    ind = n-ind
    r -= 1
    if cc=='x' or r>0:
        continue
    ba.append(ind)
    if len(ba)==k:
        break
    r = c+1

for f, b in zip(fo, reversed(ba)):
    if f==b:
        print(f)
