N=int(input())
A=list(map(int,input().split()))

destroy=0
count = 1
for i in range(N):
  if A[i] != count:destroy += 1
  else:count+=1

if destroy==N:print(-1)
else:print(destroy)