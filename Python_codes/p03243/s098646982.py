N = int(input())
for i in range(N,1000):
  I = str(i)
  if I[0] == I[1] and I[1] == I[2]:
    print(i)
    break