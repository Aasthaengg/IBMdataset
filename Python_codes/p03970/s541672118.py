c=0
S=input()
for i in range(len(S)):
  if S[i] != "CODEFESTIVAL2016"[i]:
    c=c+1
print(c)