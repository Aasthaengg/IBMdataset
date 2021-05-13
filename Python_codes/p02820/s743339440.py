n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()
def score(x):
    if x=='r':
        return p
    elif x=='s':
        return r
    else:
        return s
totalscore=0
zero=[0]*(n+1)
for i in range(n):
    if i<=k-1:
        totalscore+=score(t[i])
    else:
        if t[i]!=t[i-k]:
            totalscore+=score(t[i])
        else:
            if zero[i-k]!=0:
                totalscore+=score(t[i])
            else:
                zero[i]=1
                
                
print(totalscore)