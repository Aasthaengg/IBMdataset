N = list(map(int, list(input())))

if N[1] < N[0]:
  print(N[0] * 111)
elif N[1] > N[0]:
  print((N[0]+1) * 111)
else:
  if N[2] <= N[0]:
    print(N[0] * 111)
  else:
    print((N[0]+1) * 111)

