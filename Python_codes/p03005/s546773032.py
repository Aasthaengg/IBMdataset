inA = input().split(" ")
N = int(inA[0])
K = int(inA[1])
if(K == 1 or K == 0):
  print(0)
else:
  print((N-(K-1))-1)