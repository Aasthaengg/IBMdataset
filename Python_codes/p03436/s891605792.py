import sys
H,W=map(int,input().split())
L = [[0 for j in range(W)] for i in range(H)]
c=0
for i in range(H):
  a=list(input())
  c+=a.count(".")
  L[i]=a
#幅優先探索？
subete=[[0,0]]
ans = [[] for i in range(H*W+1)]
ans[0].append([0,0])
for i in range(H*W+1):
  for j in range(len(ans[i-1])):
    a,b=ans[i-1][j][0],ans[i-1][j][1]
    if a+1!=H:
      if [a+1,b] not in subete and L[a+1][b]==".":
        ans[i].append([a+1,b])
        subete.append([a+1,b])
    if a!=0:
      if [a-1,b] not in subete and L[a-1][b]==".":
        ans[i].append([a-1,b])
        subete.append([a-1,b])
    if b+1!=W:
      if [a,b+1] not in subete and L[a][b+1]==".":
        ans[i].append([a,b+1])
        subete.append([a,b+1])
    if b!=0:
      if [a,b-1] not in subete and L[a][b-1]==".":
        ans[i].append([a,b-1])
        subete.append([a,b-1])
  if [H-1,W-1] in subete:
    print(c-i-1)
    sys.exit()
print(-1)