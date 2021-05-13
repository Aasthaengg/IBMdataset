N = int(input())
A = list(map(int,input().split()))
cnt = 0
while(1):
  exit = False
  for i in range(len(A)):
    if(A[i]%2 == 1): 
      exit = True
  if(exit == True): break
  for i in range(len(A)):
    A[i] /= 2
  cnt += 1
print(cnt)