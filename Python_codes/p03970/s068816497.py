S=input()
A="CODEFESTIVAL2016"
c=0
for i in range(16):
  if S[i]!=A[i]:
    c+=1
print(c)