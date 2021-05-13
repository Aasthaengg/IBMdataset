A = [int(input())]

for n in range(2,10**6):
  if A[-1]%2==0:
    if A[-1]//2 in A:
      print(n)
      exit()
    else:
      A.append(A[-1]//2)
  else:
    if 1+3*A[-1] in A:
      print(n)
      exit()
    else:
      A.append(1+3*A[-1])