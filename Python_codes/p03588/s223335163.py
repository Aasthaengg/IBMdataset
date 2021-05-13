N = int(input())
if(N == 1):
  A1,B1 = map(int,input().split())
  print(str(A1+B1))
  exit()
for i in range(N-1):
  if(i == 0):
    A1,B1 = map(int,input().split())
    A2,B2 = map(int,input().split())
    if(A1 <= A2):
      MA = A2
      MB = B2
    else:
      MA = A1
      MB = B1
    A1 = A2
    B1 = B2
  else:
    A2,B2 = map(int,input().split())
    if(MA <= A2):
      MA = A2
      MB = B2
    A1 = A2
    B1 = B2
print(str(MA + MB))
