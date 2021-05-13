n = int(input())
for k in range(1,400):
  if n*k%360 == 0:
    print(k)
    break