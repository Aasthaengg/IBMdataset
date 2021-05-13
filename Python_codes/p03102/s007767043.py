N,M,C=map(int,input().split())
ListB = list(map(int, input().split()))
ListA = []
for i in range (N):
  ListA.append(list(map(int, input().split())))
res =0
mid = 0
for i in range(N):
  for j in range(M):
    mid += ListA[i][j]*ListB[j]
  mid += C
  if mid > 0:
    res+=1
  mid = 0
print(res)