R,G,B,N=map(int, input().split())
r=N//R
cnt=0
for i in range(r+1):
  NN=N-R*i
  g=NN//G
  for j in range(g+1):
    NNN=NN-G*j
    if NNN%B==0:
      cnt+=1
print(cnt)