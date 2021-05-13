def Xok():
    s=set([xp])
    for i in X:
        tmp=set()
        for c in s:
            tmp.add(c+i)
            tmp.add(c-i)
        s=tmp
    return True if x in s else False
def Yok():
    s=set([0])
    for i in Y:
        tmp=set()
        for c in s:
            tmp.add(c+i)
            tmp.add(c-i)
        s=tmp
    return True if y in s else False

s=input()
N=len(s)
x,y=map(int,input().split())

xp,X,Y=0,[],[]

i=0
while(i<N and s[i]!='T'):
    xp+=1
    i+=1
i+=1
flag=True
while(i<N):
    j=i
    cnt=0
    while(j<N and s[j]!='T'):
        cnt+=1
        j+=1
    if flag:
        Y.append(cnt)
    else:
        X.append(cnt)
    i=j+1
    flag=not flag

print('Yes' if Xok() and Yok() else 'No')