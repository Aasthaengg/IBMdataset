d = int(input())
C = list(map(int, input().split()))
S = list(list(map(int, input().split())) for i in range(d))
T = list(int(input()) - 1 for i in range(d))

kaisai = [0] * 26
manzoku = 0
date = 0
for t in T:
    date += 1
    kaisai[t] = date
    manzoku += S[date - 1][t]

    for i in range(26):
        manzoku -= C[i] * (date - kaisai[i])
    
    print(manzoku)
