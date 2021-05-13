odd=["R","U","D"]
even=["L","U","D"]
S=input()
i=0
for x in range(len(S)):
  if x%2==0 and S[x] in odd:
    i+=1
  elif x%2==1 and S[x] in even:
    i+=1
if i==len(S):
  print("Yes")
else:
  print("No")