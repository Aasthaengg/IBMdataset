def f(s):
    return abs(int(s))

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

s=input()
X,Y=map(int,input().split())
x,y=[],[]
d,tmp=0,0
for i in range(len(s)):
    if s[i]=="T":
        if tmp!=0:
            if d==0: x.append(tmp)
            else: y.append(tmp)
        d^=1
        tmp=0
        
    else: tmp+=1
if tmp!=0:
    if d==0: x.append(tmp)
    else: y.append(tmp)


if s[0]=="F": X=abs(X-x.pop(0))
Y=abs(Y)


print("Yes" if cul(x,X) and cul(y,Y) else "No")