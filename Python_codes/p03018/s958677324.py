s=input()
s=s.replace("BC","D")
s=s.replace("B","E")
s=s.replace("C","E")
s=s.split("E")

t=[]
for ss in s:
  if len(ss)!=0:
    t.append(ss)
ans=0

for tt in t:
  d_cnt=0
  for i,ttt in enumerate(tt):
    if ttt=="D":
      ans+=i-d_cnt
      d_cnt+=1
print(ans)