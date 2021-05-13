import sys
input = sys.stdin.readline

n = int(input())

bt, bx, by = 0, 0, 0
cond = True
for i in range(n):
    t, x, y = [int(w) for w in input().split()]
    dt = t-bt
    dist = abs(bx-x)+abs(by-y)
    if dt >= dist and (dt-dist) % 2 == 0:
        bt, bx, by = t, x, y
        continue
    cond = False


print("Yes" if cond else "No")
