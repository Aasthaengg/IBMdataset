N = input()
if all([n == '9' for n in N]):
  print(9 * len(N))
else:
  print(max(9 * (len(N) - 1) + (int(N[0]) - 1), sum(list(map(int, N)))))