import sys
input = sys.stdin.readline
H,W,K=map(int,input().split())
s=[[0 for e in range(W)] for f in range(H)]
for  i in range(H):
 s[i]=[d for d in input()]
ans=[[0 for e in range(W)] for f in range(H)]
iti=0
kazu=[0]*H
for i in range(H):
 if "#" in s[i]:
  kazu[i]=1
 else:
  kazu[i]=0
for  i in range(H):
 if kazu[i]==1:
  iti+=1
  fg=0
  for  j in range(W):
   if s[i][j]=="#" :
    fg+=1
    if fg>1:
     iti+=1
   ans[i][j]=iti
for  i in range(1,H):
 if kazu[i]==0:
  for  j in range(W):
   ans[i][j]=ans[i-1][j]
for  i in range(H-1)[::-1]:
 if kazu[i]==0:
  for  j in range(W):
   ans[i][j]=ans[i+1][j]
for  i in range(H):
 print(*ans[i])