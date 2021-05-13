N,M,C=map(int,input().split())
B = list(map(int,input().split()))
As=[]
for i in range(N):
  As.append(list(map(int,input().split())))
co = 0
for i in range(N):
  d = 0
  for j in range(M):
    d+= As[i][j]*B[j]
  d+=C
  if d > 0:
    co+=1
print(co)