s=input()

s2list=list(s.replace("BC","D"))
#print(s2list)

block_list=[]
bl=[]
for s2 in s2list:
  if s2=="A" or s2=="D":
    bl.append(s2)
  else:
    if len(bl)>0:
      block_list.append("".join(bl))
      bl=[]
else:
  if len(bl)>0:
    block_list.append("".join(bl))
#print(block_list)

answer=0
for bl in block_list:
  #print(bl)
  cnt_a=0
  for c in bl:
    if c=="A":
      cnt_a+=1
    else:
      answer+=cnt_a
    
print(answer)