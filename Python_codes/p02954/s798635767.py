from collections import Counter
S = input()

check_str = 'LR'
S_=[]
s_temp = ''
for s in range(len(S)):
    s_temp += S[s]
    
    if s < len(S)-1:
        s_= s+1 
        if S[s]=='L' and S[s_] == 'R':
            S_.append(Counter(s_temp))
            s_temp =''
            
    else:
        S_.append(Counter(s_temp))

def get_ans_temp(S_temp):
    S_R = S_temp['R']
    S_L = S_temp['L']
    
    S_R_ans=[0]*S_R
    S_L_ans=[0]*S_L
    
    if (S_R + S_L) % 2 ==0 :#偶数の時
        S_R_ans[-1] = (S_R + S_L) // 2
        S_L_ans[0] = (S_R + S_L) // 2

    elif S_R != S_L :#奇数の時
        if S_R > S_L:
            S_R_ans[-1] = (S_R + S_L) // 2 +1
            S_L_ans[0] = (S_R + S_L) // 2         
        else:
            S_R_ans[-1] = (S_R + S_L) // 2
            S_L_ans[0] = (S_R + S_L) // 2 + 1
            
        max_RL_num = max(S_R,S_L)
        if max_RL_num % 2 == 0:
            _ = S_R_ans[-1]
            S_R_ans[-1]=S_L_ans[0]
            S_L_ans[0]=_

    ans_temp = []
    ans_temp.extend(S_R_ans)
    ans_temp.extend(S_L_ans)
    return ans_temp

ans_list=[]
for S_temp in S_:
    ans_list.extend(get_ans_temp(S_temp))
    
ans=' '.join(map(str,ans_list))

print(ans)