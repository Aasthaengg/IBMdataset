# 初期入力
N,K = (int(x) for x in input().split())
S = input()

#
count_Lr =0 #不幸な人 LR
count_Rl =0 #不幸な人 RL
haji =0
for i in range(N-1):
    s =S[i:i+2]
    if s =="LR":
        count_Lr +=1
    if s =="RL":
        count_Rl +=1
#幸福な人 = 人と人の間の数 -不幸な人
happy_start =len(S) -1 -count_Lr -count_Rl 

change_kanou_num = min(count_Lr,count_Rl,K)
increase = change_kanou_num *2 
if change_kanou_num <K:         #Kが余っていれば、全員同じ向きを向く
    increase += abs(count_Lr -count_Rl)

happy_finsh = happy_start + increase
print(happy_finsh)