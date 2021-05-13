N,T=map(int,input().split())
tlst=list(map(int,input().split()))
value=0
mae=0
for i in range(1,N):
    value+=min(tlst[i]-tlst[i-1],T)

value+=T
print(value)
