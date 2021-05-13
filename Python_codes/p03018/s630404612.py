s=input()
s=s.replace("BC","D")
m=[]
is_seq=False
t=""
for ss in s:
  if is_seq:
    if ss=="A" or ss=="D":
      t+=ss
    else:
      m.append(t)
      t=""
      is_seq=False
  else:
    if ss=="A":
      is_seq=True
      t+=ss
if t!="":
  m.append(t) 
# print(m)
ans=0
for mm in m:
  cnt_a=mm.count("A")
  for i in range(len(mm)):
    if mm[i]=="A":
      ans+=len(mm)-cnt_a-i
      cnt_a-=1
print(ans)

