N = list(map(int, list(input())))
for i in range(3):
  N[i] = 10 - N[i]

print(N[0]*100 + N[1]*10 + N[2])