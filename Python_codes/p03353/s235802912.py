s=list(map(str,input()))
A=int(input())
V=[]
S=[]
ct=0
for i in range(1,A+1):
  for j in range((len(s)-(i-1))):
    V.append("".join(s[j:j+i]))
S=sorted(set(V))
#print(S)
print(S[A-1])
