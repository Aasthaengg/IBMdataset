tlist=list(input())

answer_list=[]
for t in tlist:
  if t=="?":
    answer_list.append("D")
  else:
    answer_list.append(t)
    
print("".join(answer_list))