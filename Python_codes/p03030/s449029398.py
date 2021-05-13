R=list()
n=0
s=list()
p=list()
N=int(input())
for i in range(N):
  S,P=input().split()
  P=int(P)
  s.append([S,100-P,i+1])
  p.append(P)
  n=S
s=sorted(s)
for i in range(N):
  print(s[i][2])