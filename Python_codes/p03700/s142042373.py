import math
n,a,b = map(int,input().split())
hl = []
for _ in range(n):
   h = int(input())
   hl.append(h)

ub = 10**9
lb = 0
while True:
    if ub == lb:
        break
    target = (ub + lb) // 2
    need = 0
    for h in hl:
        rest = h - target * b
        need += max(math.ceil(rest / (a-b)), 0)
    if need <= target:
        ub = target
    else:
        lb = target + 1
print(lb)