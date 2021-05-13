S=input()
P=0
for i in range(len(S)):
  P+=(i&1)-(S[i]=='p')
print(P)