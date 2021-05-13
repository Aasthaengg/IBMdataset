from sys import exit
N = int(input())
A = map(int,input().split())
B = [0]*N
for i in A:
  B[i] += 1
if N%2 == 1:
  if B[0] != 1:
    print(0)
    exit()
  for i in range(1,N):
    if i%2 == 1 and B[i] != 0:
      print(0)
      exit()
    elif i%2 == 0 and B[i] != 2:
      print(0)
      exit()
else:
  for i in range(N):
    if i%2 == 1 and B[i] != 2:
      print(0)
      exit()
    elif i%2 == 0 and B[i] != 0:
      print(0)
      exit()
print(pow(2,N//2,1000000007))