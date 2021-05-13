N=int(input())
print(N*(N-1)//2-N//2)

if N%2 == 0:
  for i in range(1,N):
    for j in range(i+1,N+1):
      if i+j != N+1:
        print("{} {}".format(i,j))
else:
  for i in range(1,N):
    for j in range(i+1,N+1):
      if i+j != N:
        print("{} {}".format(i,j))