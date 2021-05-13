N,M = map(int,input().split())
A = [];B = []
for i in range(N):
  temp = str(input())
  temp = list(temp)
  A.append(temp)
for i in range(M):
  temp = str(input())
  temp = list(temp)
  B.append(temp)
#print(A,B)
for i in range(N-M+1): #0~N-M
  for j in range(N-M+1): 
    Flag = True
    for p in range(M):
      for q in range(M):
        #print(i+p,j+q,p,q)
        if A[i+p][j+q] != B[p][q]:
          Flag = False
    if Flag:
      print("Yes")
      exit()
print("No")