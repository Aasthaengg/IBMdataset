S = list(input())

#最終的にRLのところで往復することになる
#最初のLと最後のRはそこに集約される

N = len(S)

ans = list()

#最初のLの連続を集約
i = 0

if S[0] == "L":
    ans.append(0)
    while i < N:
        if S[i] == "L":
            ans[0] += 1
            if i != 0:
                ans.append(0)
        else:
            break
        i+= 1

#あとは最後まで行く
R_cnt = 0
L_cnt = 0
while i < N:
    #Rを集約
    if S[i] == "R":
        R_cnt += 1
        i += 1
    else:
        #Lを集約
        while i < N:
            if S[i] == "L":
                L_cnt += 1
                i += 1
            else:
                #RL境界の手前まで埋める
                ans += [0 for _ in range(R_cnt - 1)]
                
                #RLの値を埋める。
                #10**100移動する
                #最終移動後には、集約したRの個数のうち、R_cnt//2はLのマスへ、残りがRのマスにいる
                #最終移動後には、集約したLの個数のうち、L_cnt//2はRのマスへ、残りがLのマスにいる
                ans.append(R_cnt - (R_cnt//2) + L_cnt//2)
                ans.append(L_cnt - (L_cnt//2) + R_cnt//2)

                #RL境界以後のところをRまで埋める
                ans += [0 for _ in range(L_cnt - 1)]

                R_cnt = 0
                L_cnt = 0
                break

if R_cnt!=0:
    if L_cnt != 0:
        #...RRRLLLのような終わり方
                ans += [0 for _ in range(R_cnt - 1)]
                ans.append(R_cnt - (R_cnt//2) + L_cnt//2)
                ans.append(L_cnt - (L_cnt//2) + R_cnt//2)
                ans += [0 for _ in range(L_cnt - 1)]
    else:
        #...RRRRRRのような終わり方
        ans += [0 for _ in range(R_cnt - 1)]
        ans.append(R_cnt)

print(' '.join(map(str, ans)))