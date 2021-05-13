n=int(input())
s=input()

d=[0]*n
d2=[0]*n
d[0]=1 if s[0]=="#" else 0
d2[-1]=1 if s[-1]=="." else 0

for i in range(1,n):
  d[i]=d[i-1]+1 if s[i]=="#" else d[i-1]
  d2[-1-i]=d2[-i]+1 if s[-i-1]=="." else d2[-i]

m=n
for i in range(n):
  m=min(m,d[i]+d2[i])
print(m-1)