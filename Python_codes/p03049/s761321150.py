n=int(input())
s=[input() for i in range(n)]
ans=0
ab=a=b=0
for ss in s:
  ans+=ss.count("AB")
  if ss[0]=="B" and ss[-1]=="A":
    ab+=1
  elif ss[0]=="B" and ss[-1]!="A":
    b+=1
  elif ss[0]!="B" and ss[-1]=="A":
    a+=1
# print(ans)
cnt_min=min(a,b)
if ab==0:
  ans+=cnt_min
else:
  if a+b>0:
    ans+=ab+cnt_min
  else:
    ans+=ab-1
print(ans)
