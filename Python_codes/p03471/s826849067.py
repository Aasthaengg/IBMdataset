N, Y = map(int, input().split())
exist_comb = False
res10000 = -1
res5000 = -1
res1000 = -1

for i in range(N+1):
  for j in range(N-i+1):
    k = N-i-j
    Sum = 10000*i + 5000*j + 1000*k
    if Sum == Y:
      res10000 = i
      res5000 = j
      res1000 = k

print("{} {} {}".format(res10000, res5000, res1000))