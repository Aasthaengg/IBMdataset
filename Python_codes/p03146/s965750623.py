s = int(input())
a = [0] * 1000000
a[0] = s

for i in range(1,1000000):
  if a[i-1] % 2 == 0:
    a[i] = a[i-1]//2
  else:
    a[i] = a[i-1]*3+1
  if a[i] in a[:i]:
    print(i+1)
    exit()