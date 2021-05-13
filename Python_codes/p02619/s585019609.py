D = int(input())
c = [None] + list(map(int, input().split()))
s = [None] + [[None] + list(map(int, input().split())) for _ in range(D)]
t = [None] + [int(input()) for _ in range(D)]

S = 0
last = [0] * 27
score = 0
for d in range(1, D + 1):
    S += s[d][t[d]]
    last[t[d]] = d
    for i in range(1, 27):
        S -= c[i] * (d - last[i])
    score += max(10 ** 6 + S, 0)
    print(S)
