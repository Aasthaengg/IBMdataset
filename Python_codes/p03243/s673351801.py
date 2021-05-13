n=int(input())
l = [111*i for i in range(1,10)]
for j in l:
  if j >= n:
    print(j)
    exit()