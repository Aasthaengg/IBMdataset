n=int(input())
A=list(map(int,input().split()))
S=[A[0]]
for i in range(n-1):
  S.append(S[-1]+A[i+1])
ans1=0
s1=0
a=-1
for i in range(n):
  a=a*(-1)
  if a==1:
    ans1=ans1+max(0,1-(S[i]+s1))
    s1=s1+max(0,1-(S[i]+s1))
  else:
    ans1=ans1+max(0,S[i]+s1+1)
    s1=s1-max(0,S[i]+s1+1)
ans2=0
a=1
s2=0
for i in range(n):
  a=a*(-1)
  if a==1:
    ans2=ans2+max(0,1-(S[i]+s2))
    s2=s2+max(0,1-(S[i]+s2))
  else:
    ans2=ans2+max(0,S[i]+s2+1)
    s2=s2-max(0,S[i]+s2+1)
print(min(ans1,ans2))