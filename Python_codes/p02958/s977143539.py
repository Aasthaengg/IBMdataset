import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

targets = {}
for i in range(N):
    if P[i] != i+1:
        targets[i] = P[i]

# print(targets)
if not targets:
    print("YES")
elif len(targets) == 2:
    for i, v in targets.items():
        if v-1 in targets and targets[v-1] == i+1:
            print("YES")
        else:
            print("NO")
        break
else:
    print("NO")