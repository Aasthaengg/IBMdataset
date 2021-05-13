ss=list(input())
tt=list(input())
res=0
for s,t in zip(ss,tt):
  if s==t:
    res+=1
print(res)