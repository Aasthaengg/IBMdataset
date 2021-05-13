n=int(input())
A=list(map(int,input().split()))
cnt=0
for i in range(500000000):
  for j in range(n):
    if A[j]%2==1:
      print(cnt)
      exit();
    else:
      A[j]//=2
  cnt+=1
print(cnt)