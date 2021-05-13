S=input()
"""
#最終的にどこかに収束するはず
#Rから出発した人はLがある場所まで進み、あとはLとRで反復
Lも同様

"""
ans=[0]*len(S)
R,L=0,0
points=[]#i,i+1、R,Lの4要素リストが格納
for i in range(len(S)-1):
    if S[i]=="R" and S[i+1]=="R":#RかLが連続している
        R+=1
    elif S[i]=="L" and S[i+1]=="L":#RかLが連続している
        L+=1
    #みんなが集まるポイント
    elif S[i]=="R" and S[i+1]=="L":
        if ans[i]==0:
            ans[i]=1
        if ans[i+1]==0:
            ans[i+1]=1
        #今まで数えてきたRを足す
        ans[i]+=R//2
        ans[i+1]+=R//2+R%2#余りはもらう
        points=[i,i+1]
        R=0#R区間初期化
    #ここまで数えてきたLを前の数値に足す
    elif S[i]=="L" and S[i+1]=="R":
        if len(points)>0 and L>0:
            ans[points[0]]+=L//2+L%2#余りはもらう
            ans[points[1]]+=L//2
        L=0#L区間初期化
        points=[]
#拾い残し回収
if L>0 and len(points)>0:
    ans[points[0]]+=L//2+L%2#余りはもらう
    ans[points[1]]+=L//2

map = map(str, ans)
print(' '.join(map))