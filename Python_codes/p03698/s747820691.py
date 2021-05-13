S = list(input())
S.sort()
flag = 0
for i in range(len(S)- 1):
  if(S[i] == S[i+ 1]):
    flag = 1
    break
if(flag == 1):
  print("no")
else:
  print("yes")