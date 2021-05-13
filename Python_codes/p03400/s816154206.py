N=int(input())
D,X=map(int,input().split())
for _ in range(N):
  A=int(input())
  if D%A:
    X += D//A+1
  else:
    X += D//A
print(X)