from collections import deque

x, y, a, b, c = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P = sorted(P, reverse=True)[:x]

Q = sorted(Q, reverse=True)[:y]

P.extend(Q)
R.extend(P)

T = sorted(R, reverse=True)[:x+y]
print(sum(T))