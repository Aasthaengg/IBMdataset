N,M = map(int,input().split())
a_g=[];b_g=[]
for i in range(N):
  a_g.append(list(input()))
for i in range(M):
  b_g.append(list(input()))

for i in range(N-M+1):
  for j in range(N-M+1):
    flag=1
    for k in range(M):
      for l in range(M):
        if a_g[k+i][l+j] != b_g[k][l]:
          flag=0
          break
    if flag:
      print("Yes");exit()
print("No")