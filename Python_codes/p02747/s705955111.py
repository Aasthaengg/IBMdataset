S = input()
n=0

for i in range(len(S)//2):
  if S[2*i]+S[2*i+1]=="hi":
    n+=1
  
if n==len(S)/2:
  print("Yes")
else:print("No")