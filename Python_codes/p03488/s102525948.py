from copy import copy
s = input() + "T"
n=len(s)
x, y = map(int, input().split())

xy=[[],[]]

sgn = 1
now = n
for i in range(n):
    if s[i] == "T":
        x -= i
        now = i + 1
        break
for i in range(now, n):
    if s[i] == "T":
        xy[sgn].append(i - now)
        now = i + 1
        sgn ^= 1


cur = {0}
for i in xy[0]:
    nxt = set()
    for j in cur:
        nxt.add(j + i)
        nxt.add(j - i)
    cur = copy(nxt)

flag = x in cur

cur = {0}
for i in xy[1]:
    nxt = set()
    for j in cur:
        nxt.add(j + i)
        nxt.add(j - i)
    cur = copy(nxt)

print("Yes" if flag and y in cur else "No")