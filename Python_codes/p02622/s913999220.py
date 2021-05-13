S=input()
T=input()
S=list(S)
T=list(T)
a=0
b=len(S)
for i in range(b):
  if S[i]!=T[i]:
    a+=1
print(a)