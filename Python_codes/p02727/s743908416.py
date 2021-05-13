from collections import deque

X, Y, A, B, C = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)
q = sorted(list(map(int, input().split())), reverse=True)
r = sorted(list(map(int, input().split())), reverse=True)

cand = sorted(p[:X] + q[:Y] + r, reverse=True)
print(sum(cand[:X+Y]))
