import sys
from collections import Counter
N = int(input())
D = Counter(map(int, input().split()))

M = int(input())

for t in map(int, input().split()):
    if t in D:
        if D[t] > 0:
            D[t] -= 1
        else:
            print("NO")
            exit()
    else:
        print("NO")
        exit()

print("YES")

