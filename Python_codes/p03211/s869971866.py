d = input()
dL = len(d)
dE = dL - 3
Min = 10000000000

for i in range(0, dE+1):
  D = int(d[i:i+3])
  J = abs(D - 753)
  if J < Min:
    Min = J

print(Min)