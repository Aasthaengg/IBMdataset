a = [int(x) for x in input().split()]
for i in range(5):
  if a[i] == 0:
    print(i+1)
    exit(0)