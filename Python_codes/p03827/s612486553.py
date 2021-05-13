N=int(input())
S=input()
a=0
L=[0]
for i in range(N):
  if S[i]=="I":
    a+=1
  else:
    a-=1
  L.append(a)
print(max(L))