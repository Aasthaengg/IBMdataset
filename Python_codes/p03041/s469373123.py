N,K=map(int,input().split())
S=input()
a=S[0:K-1]
b=S[K:]
c=S[K-1]
c=c.lower()
print(a+c+b)