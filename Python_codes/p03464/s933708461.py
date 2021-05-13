
import sys
input = sys.stdin.readline

K = int(input())
A = list(map(int, input().split()))

lb, ub = 1, 10**18
while ub - lb > 1:
    m = (lb + ub) // 2
    rem = m
    for a in A:
        rem = rem // a * a
    if rem < 2:
        lb = m
    else:
        ub = m

lb2, ub2 = 1, 10**18
while ub2 - lb2 > 1:
    m = (lb2 + ub2) // 2
    rem = m
    for a in A:
        rem = rem // a * a
    if rem <= 2:
        lb2 = m
    else:
        ub2 = m

if ub > lb2:
    print(-1)
else:
    print(ub, lb2)