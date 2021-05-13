D = int(input())
c = [int(x) for x in input().split()]
s = [input().split() for l in range(D)]
t = []
for i in range(D):
    t += [int(input())]
manzoku = 0
d = 1
last = [0]*26

for p in range(D):
    #タイプはt[p]-1,0~25 満足度増加 s[p][t[p]] p+1日目
    manzoku += int(s[p][t[p]-1])
    last[t[p]-1] = p+1
    for i in range(26):
        manzoku -= c[i] *(p+1-last[i])
    print(manzoku)