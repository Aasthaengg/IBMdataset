MOD = 1000000007
N = int(input())
S1 = list(input())
S2 = list(input())

if S1[0] == S2[0]:
    ans = 3
    tmp = True #直前が縦
    j = 1 #次に見始めるところ
else:
    ans = 6
    tmp = False
    j = 2

while j < N:
    if S1[j] == S2[j]: #縦に並んでいる時
        if tmp: #縦が連続の時
            ans *= 2
        else: #直前が横
            ans *= 1
        tmp = True
        j += 1
    else: #横に並んでいる時
        if tmp: #縦-->横のとき
            ans *= 2
        else: #横が連続の時
            ans *= 3
        tmp = False
        j += 2
    ans %= MOD

print (ans)
