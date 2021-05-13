d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
t = [int(input()) for _ in range(d)]

manzoku = 0
log = [-1] * 26
for i in range(d):
    q = t[i]-1
    manzoku += s[i][q]
    log[q] = i
    for j in range(26):
        manzoku -= c[j] * (i-log[j])
    print(manzoku)
