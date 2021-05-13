# bit全順列列挙
def bitall(n):
    parm = []
    for i in range(1<<n): # 0/1の組み合わせは1<<n(=2**n)通り存在。
        on = [0 for _ in range(n)] # とりあえず全て0にしておく。
        
        for j in range(n):
            if i & (1<<j): # iのj桁目が1となっている場所をonにする。
                on[j] = 1
                
        parm.append(on)
                
    return parm


N, M = map(int, input().split())
K = []
S = []
for m in range(M):
    tmp = list(map(int, input().split()))
    K.append(tmp[0])
    S.append(tmp[1:])
P = list(map(int, input().split()))

swi_parms = bitall(N)
ans =0

for swi_parm in swi_parms:
    flag = 0
    for k in range(len(K)):
        cnt = 0
        
        for s in S[k]:
            # 対応するスイッチのon数をカウント
            if swi_parm[s-1] == 1: cnt += 1
        
        if cnt%2 == P[k]:
            continue
        else:
            flag = 1
            break
    if flag == 0:
        ans += 1

print(ans)