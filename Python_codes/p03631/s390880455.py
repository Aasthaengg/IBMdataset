N = input()

rev_N = N[2] + N[1] + N[0]

if int(N) == int(rev_N):
  print("Yes")
else:
  print("No")