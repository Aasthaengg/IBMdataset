S=input()
W=[0]*(len(S)+1)
W[0]=1
words=['dream','dreamer','erase','eraser' ]
for i in range(len(S)):
  if W[i]==0:
    continue
  for k in words:
    if S[i:i+len(k)]==k:
      W[i+len(k)]=1
if W[len(S)]==1:
  print("YES")
  exit()
else:
  print("NO")
