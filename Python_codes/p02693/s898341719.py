K=int(input())
A,B=map(int,input().split())
a=0
for i in range(A,B+1):
  if i%K==0:
    a=1
if a==1:
  print("OK")
else:
  print("NG")
    
