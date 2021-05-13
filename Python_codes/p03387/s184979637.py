A = list(map(int,input().split()))
A = sorted(A)
cnt = 0

if A[1]-A[0]>=2:
  cnt += (A[1]-A[0])//2
  A[0]+= cnt*2

if A[0]==A[1] and A[1]==A[2]:
  print(cnt)
  exit()

  
while(True):
  cnt+=1
  A = sorted(A)
  A[0]+=1
  A[1]+=1
  #print(A)
  if A[0]==A[1] and A[1]==A[2]:
    break

print(cnt)