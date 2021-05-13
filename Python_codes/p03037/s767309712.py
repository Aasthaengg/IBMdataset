n,m=map(int,input().split())
L=[0]*m
R=[0]*m
table=[0]*(n+2)
for i in range(m):
   L[i],R[i]=map(int,input().split())
   table[L[i]]+=1
   table[R[i]+1]-=1
s=[0]*(n+2)#累積和をするリスト
for i in range(1,n+2):
   s[i]=s[i-1]+table[i]
print(s.count(m))