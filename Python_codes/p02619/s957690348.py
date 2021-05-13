D = int(input())
c = list(map(int, input().split()))
s = []
for _ in range(D):
    s.append(list(map(int, input().split())))
t = [(int(input()) - 1) for _ in range(D)]

last = [0] * 26

S = 0
for dd in range(1, D + 1):
    S += s[dd - 1][t[dd - 1]]
    last[t[dd - 1]] = dd
    for i in range(26):
        S -= c[i] * (dd - last[i])
    print(S)
