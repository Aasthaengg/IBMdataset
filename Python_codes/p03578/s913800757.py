import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

counter = Counter(D)
for t_i in T:
    if t_i in counter and 0 < counter[t_i]:
        counter[t_i] -= 1
    else:
        print("NO")
        sys.exit()

print("YES")