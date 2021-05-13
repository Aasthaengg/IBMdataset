N,Y = input().split()
N,Y = map(int,(N,Y))
Z = Y
for i in range(N+1):
  Y = Y-10000*i
  for j in range(N+1-i):
    Y = Y-5000*j
    Y = Y-1000*(N-i-j)
    if Y == 0:
      print(i,end = " ")
      print(j,end = " ")
      print(N-i-j,end = " ")
      break
    else :
      Y=Z-i*10000
  else:
    Y = Z
    continue
  break
else :
  print(-1,end=" ")
  print(-1,end=" ")
  print(-1,end=" ")