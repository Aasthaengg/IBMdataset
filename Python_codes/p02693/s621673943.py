K=int(input())
A,B=map(int,input().split())
t=B-A+1
for x in range(t):
  if A%K==0:
    print("OK")
    break
  else:
    A += 1
if A>B:
  print("NG")