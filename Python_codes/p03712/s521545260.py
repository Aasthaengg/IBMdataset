H,W=map(int,input().split())
t=''
s=[]
for i in range(W+2):
  t+='#'
s.append(t)
for i in range(H):
  a='#'+input()+'#'
  s.append(a)
s.append(t)
for i in range(H+2):
  print(s[i])