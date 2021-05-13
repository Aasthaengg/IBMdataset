import sys
from sys import stdin

n = int(stdin.readline().rstrip())
a, b = map(int, stdin.readline().rstrip().split())
p = list(map(int, stdin.readline().rstrip().split()))
ans1 = 0
ans2 = 0
ans3 = 0
p.sort()

for pi in p:
    if pi <= a:
        ans1 += 1
    elif pi > a and pi <= b:
        ans2 += 1
    else:
        ans3 += 1

print(min(ans1, ans2, ans3))