
import itertools
S = input()
RevS = reversed(S)
L = [0]#左の<
R = [0]#右の>
cur = 0
for s in S:
    if s == "<":
        cur += 1
    else:
        cur = 0
    L.append(cur)
cur = 0
for r in RevS:
    if r == ">":
        cur += 1
    else:
        cur = 0
    R.append(cur)
R.reverse()
ans = 0
for n in range(len(S)+1):
    ans += max(L[n],R[n])
print(ans)