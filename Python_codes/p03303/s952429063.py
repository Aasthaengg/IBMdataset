S=list(input())
w=int(input())

answer_list=[]
for i in range(0,len(S),w):
  #print(S[i])
  answer_list.append(S[i])
  
print("".join(answer_list))