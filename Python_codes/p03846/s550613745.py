N=int(input())
A=list(map(int,input().split()))
A.sort()
if N % 2 == 0:
  for i in range(1,N,2):
    for n in range(2):
      if not A[i + n - 1] == i:
        print(0)
        exit()
  print(2**(N//2)%1000000007)
else:
  for i in range(0,N-1,2):
      for n in range(2):
        if i == 0 and n == 0:
          continue
        if not A[i + n - 1] == i:
          print(0)
          exit()
  print(2**((N-1)//2)%1000000007)