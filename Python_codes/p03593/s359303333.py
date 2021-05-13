h,w=map(int,input().split())

a=[]
for i in range(h):
  a.append(input())

alpha=[0 for i in range(26)]

for i in range(h):
  for j in range(w):
    alpha[ord(a[i][j])-ord("a")]+=1


l=[0,0,0]
for i in range(26):
  l[0]+=alpha[i]//4
  alpha[i]=alpha[i]%4
  l[1]+=alpha[i]//2
  alpha[i]=alpha[i]%2
  l[2]+=alpha[i]
  alpha[i]=0

if l[1]<=(h//2)*(w%2)+(w//2)*(h%2) and l[2]==(h%2)*(w%2):
  print("Yes")
else:
  print("No")
