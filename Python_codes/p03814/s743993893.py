S=list(input())

start=-1
last=-1

for i in range(len(S)):
  if S[i]=="A":
    start=i
    break

for j in reversed(range(0,len(S))):
  if S[j]=="Z":
    last=j
    break

print(last-start+1)
