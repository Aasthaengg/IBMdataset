f=lambda:[*map(int,input().split())]
d=int(input())
c=f()
S,t=[],[]
for i in range(d): S+=[f()]
for i in range(d): t+=[int(input())]
v=0
D=[0]*26
for i in range(d):
  D[t[i]-1]=i+1
  v+=S[i][t[i]-1]
  for j in range(26):
    v-=c[j]*(i+1-D[j])
  print(v)