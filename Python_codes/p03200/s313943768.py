S=input()
ans=0
b_cnt=0
for i in range(len(S)):
  if S[i]=="B":
    b_cnt+=1
  else:
    ans+=b_cnt
print(ans)
