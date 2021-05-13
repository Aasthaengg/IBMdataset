N=int(input())
S=input()
s=""
m=""
ss=[]
mm=[]
s1=set()
m1=set()
res = 0
for i in range(N):
  s=S[0:i+1]
  m=S[i+1:N]
  ss=list(s)
  mm=list(m)
  s1=set(ss)
  m1=set(mm)
  s_intersection = s1 & m1
  res= max(res,len(s_intersection))
print(res)