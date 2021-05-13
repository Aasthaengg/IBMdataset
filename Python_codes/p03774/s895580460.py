import sys
input = sys.stdin.readline
n, m = [int(w) for w in input().split()]
ls = [[int(w) for w in input().split()] for _ in range(n)]
lp = [[int(w) for w in input().split()] for _ in range(m)]

for a, b in ls:
    ans = -1
    dist = 10e10
    for i, (c, d) in enumerate(lp):
        d = abs(a-c) + abs(b-d)
        if d < dist:
            ans = i
            dist = d
    print(ans+1)
