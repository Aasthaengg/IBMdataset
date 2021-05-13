from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
sm = 0
d = defaultdict(int)
for a in A:
    d[a] += 1
    sm += a
Q = int(input())
for _ in range(Q):
    b,c = map(int,input().split())
    sm += d[b]*(c-b)
    d[c] += d[b]
    d[b] = 0
    print(sm)