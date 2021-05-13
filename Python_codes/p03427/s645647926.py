N = input()
N_row = len(N)
while True:
  if N_row == 1:
    print(int(N))
    break
  else:
    N = list(N)
    a = int(N[0])
    b = int(N[-1])
    for i in range(1, N_row):
      if not int(N[i]) == 9:
        sum = (a-1) + 9*(N_row-1) 
        print(sum)
        break
    else:
      sum = a + 9*(N_row-1)
      print(sum)
      break
  break