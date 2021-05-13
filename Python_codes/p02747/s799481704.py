S = list(input())
a = len(S)
b = 0
c = 0
for i in range(a):
  if i%2==0:
    if(S[i] == "h"):
      b+=1
  else:
    if(S[i]=="i"):
      c+=1
if(b+c==a and b==c):
  print("Yes")
else:
  print("No")