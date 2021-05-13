n,k=map(int,input().split())
S=input()
c=0
d=0
for i in range(n-1):
    if S[i]==S[i+1]:
        c+=1
    if S[i]!=S[i+1]:
        d+=1
d=(d+1)//2
print(c+2*d-1 if (d<=k and S[0]!=S[-1]) else c+2*min(d,k))