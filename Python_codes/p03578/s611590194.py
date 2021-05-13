from collections import Counter

N = int(input())
D = [int(_) for _ in input().split()]
M = int(input())
T = [int(_) for _ in input().split()]

cntd = Counter(D)
cntt = Counter(T)

for t in cntt:
    if cntt[t] > cntd[t]:
        print("NO")
        exit(0)
print("YES")
