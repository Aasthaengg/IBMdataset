P=[]
C=[]
point=1001    #全問題数
 
D,G=map(int,input().split())
for i in range(D):
    p,c= map(int,input().split())
    P.append(p)
    C.append(c)
 
#とりあえず全部解くor解かないで目標スコアを超えるか超えないかを考える
 
 
for i in range(2**D) :
    score=0
    solve=0
    needproblem=0
    for j in range(D) :                  #全正解した大問をスコアに変換
        if (i>>j) & 1 :
            score+=P[j]*100*(j+1)+C[j]
            solve+=P[j]
        if (~i>>j) & 1 :                  #1問も解かなかった問題の中で最も一題あたりの点が高い問題
            needproblem=j+1
    if score>=G :
        point=min(point,solve)
 
#ぎりぎりスコアが届いていない場合、1問も解かなかった問題の中で最も一題あたりの点が高い問題だけ解いてみる
#中途半端に大問を解ききるのが１種類以下でも目標に届く場合もあるという予想
 
    elif score<G :                
        rest=G-score
        sum=(P[needproblem-1]-1)*needproblem*100
        if rest>sum :            #1問も解かなかった問題の中で最も一題あたりの点が高い問題を解いても届かないのでやり直し
            continue
        elif rest<=sum :
            resolve=solve+(rest//(needproblem*100)+(rest%(needproblem*100)>0))
            point=min(point,resolve)
 
print(point)