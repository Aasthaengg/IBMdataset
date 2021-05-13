from collections import defaultdict

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))
Ddic = defaultdict(int)
Tdic = defaultdict(int)

for d in D:
    Ddic[d] += 1
for t in T:
    Tdic[t] += 1
for n, v in Tdic.items():
    Ddic[n] -= v
dv = Ddic.values()
if all(i >= 0 for i in dv):
    print("YES")
else:
    print("NO")