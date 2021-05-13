s,t,answer = input(),input(),0
for i,j in enumerate(s):
  if j != t[i]:
    answer += 1
    
print(answer)