S = str(input())
K = int(input())
s  = ""
for i in range(len(S)):
  if(S[i]=="1"):
    s += S[i]
  else:
    s+=S[i]
    break
if(K>=len(s)):
  print(s[-1])
else:
  print("1")