n,m=map(int,input().split())
arr = list(map(int, input().split()))
A=[]
suM=0
for i in arr:
  A.append(i)
for i in A:
  suM+=i
if suM>n:
  print(-1)
elif (suM==n) or (suM<n):
  print(n-suM)
