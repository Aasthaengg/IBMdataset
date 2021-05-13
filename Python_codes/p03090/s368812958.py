N = int(input())

print((((N-1)*N)//2) - N//2)


if N % 2 == 1:
  ban = N
else:
  ban = N + 1


for i in range(1,N):
  for j in range(i+1,N+1):
    if i + j != ban:
      print(i,j)