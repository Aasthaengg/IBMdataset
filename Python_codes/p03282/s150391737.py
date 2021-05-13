S=input()
K=int(input())
i=0
while S[i]=='1' and K>i+1 and i<len(S):
  i+=1
if i==len(S):
  i=0
print(S[i])
