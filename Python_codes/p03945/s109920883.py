S = list(input())
c=0
first = S[0]
for i in range(1,len(S)):
  if S[i] != first:
    c+=1
    first = S[i]
print(c)
   
