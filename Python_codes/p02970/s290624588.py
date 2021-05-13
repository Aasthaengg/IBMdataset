s1,s2=input().split()
N=int(s1)
D=int(s2)
n=N
ans=0
while n>0:
  n=n-(2*D+1)
  ans=ans+1
print(ans)
