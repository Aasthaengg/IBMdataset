n,m=map(int,input().split())
a=list(map(int,input().split()))

s=[0]*n
s[0]=a[0]%m
for i in range(1,n):
    s[i]=(s[i-1]+a[i])%m
    
t=dict()
for i in range(n):
    si=s[i]
    if si in t:
        t[si]+=1
    elif si==0:
        t[0]=2
    else:
        t[si]=1
        
icnt=0
for v in t.values():
    icnt+=v*(v-1)//2

print(icnt)
