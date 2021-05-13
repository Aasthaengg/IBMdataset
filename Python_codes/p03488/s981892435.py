def cul(x,X):
    dic={0:1}
    for i in range(len(x)):
        tmp={}
        for j in dic:
            tmp[j+x[i]]=1
            tmp[j-x[i]]=1
        dic=tmp
    if X in dic: return True
    else: return False

S=input()
s=list(S.split("T"))
X,Y=map(int,input().split())
x,y=[len(i) for i in s[::2]],[len(i) for i in s[1::2]]
if S[0]=="F": X=abs(X-x.pop(0))
Y=abs(Y)

dx=sorted(x,reverse=True)
dy=sorted(y,reverse=True)

print("Yes" if cul(dx,X) and cul(dy,Y) else "No")