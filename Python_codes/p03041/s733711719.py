n,k=map(int,input().split())
s=input()

S=list(s)
a=S[k-1]
b=a.lower()
S[k-1]=b

print(*S,sep='')
