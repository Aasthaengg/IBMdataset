N=int(input())
S=input()
c=0
if len(S)>2:
  for i in range(1,N-1):
    if S[i-1]=="A" and S[i]=="B" and S[i+1]=="C":
      c+=1
print(c)