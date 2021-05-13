N=int(input())
S=str(input())
x,ans=0,0
for i in range(N):
    if S[i]=="I":
        x+=1
        if ans<x:
            ans=x
    elif S[i]=="D":
        x-=1

print(ans)