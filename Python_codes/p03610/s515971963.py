S=list(input())
L=list()
for i in range(len(S)):
  if i%2==0:
    L.append(S[i])
print("".join(L))