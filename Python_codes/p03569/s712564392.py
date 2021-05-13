S=input()
_S=[]
for s in S:
    if s != "x":
        _S.append(s)
len_S=len(_S)
if  sum([_S[i]!=_S[-i-1] for i in range(len_S//2)]):
    print(-1)
else:
    count=0
    i,m=0,len(S)-1
    while m-i>0:
        if S[i]=="x" and S[m]!="x":
            i+=1
            count+=1
        elif S[i]!="x" and S[m]=="x":
            m-=1
            count+=1
        else:
            i+=1
            m-=1
    print(count)
