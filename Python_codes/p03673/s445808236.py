from collections import deque
import sys
input = sys.stdin.buffer.readline


n = int(input())
A = [int(i) for i in input().strip().split()]

b = deque()

flag = True

if n % 2 == 1:
    flag = False
for a in A:
    if flag:
        b.append(a)
    else:
        b.appendleft(a)
    flag = not flag

print(" ".join((str(s) for s in b)))
