x = list(map(int,input().split()))

for i in range(3):
  if x.count(x[i]) == 1:
    print(x[i])
    exit()