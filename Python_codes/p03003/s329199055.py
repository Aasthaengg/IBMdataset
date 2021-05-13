def i1():
 return int(input())
def i2():
 return [int(i) for i in input().split()]

[n,m]=i2()
s=i2()
t=i2()
x=10**9+7
cs=[[0 for i in range(2*10**3)]for j in range(2*10**3)]
y=0
for i in range(n):
 if s[i]==t[0]:
   y+=1
 cs[i][0]=y+0
y=0
for i in range(m):
 if s[0]==t[i]:
   y+=1
 cs[0][i]=y+0
for i in range(1,n):
 for j in range(1,m):
  if s[i]==t[j]:
   cs[i][j]=(cs[i-1][j]+cs[i][j-1]+1)%x
  else:
   cs[i][j]=(cs[i-1][j]+cs[i][j-1]-cs[i-1][j-1])%x
print((cs[n-1][m-1]+1)%x)