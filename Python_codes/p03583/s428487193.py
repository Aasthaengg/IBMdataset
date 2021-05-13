N = int(input())

if N % 2 == 0:
  print(N//2, N, N)
else:
  for i in range(1, N):
    if N < 4*i:
      n = 4*i - N
      break
  if n == 1:
    j, k = 2*N*i, 2*N*i
  else:
    if i % 3 == 0:
      j, k = 2*N*i//3, 2*N*i//3
    else:
      for x in range(100):
        flag = False
        for y in range(1, n//2+1):
          if ((N*i)%y==0) and ((N*i)%(n-y)==0):
            j = (N*i) // y
            k = (N*i) // (n-y)
            flag = True
            break
        if flag:
          break
        else:
          i += 1
          n += 4
  print(i, j, k)