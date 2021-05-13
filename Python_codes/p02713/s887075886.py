K = int(input())

total = 0
for i in range(1,K+1,1):
  for j in range(1,K+1,1):
    tmp1 = i
    tmp2 = j
    while tmp1 % tmp2 != 0:
      tmp = tmp1 % tmp2
      tmp1 = tmp2
      tmp2 = tmp
    for k in range(1,K+1,1):
      tmp1 = k
      tmp3 = tmp2
      while tmp1 % tmp3 != 0:
        tmp = tmp1 % tmp3
        tmp1 = tmp3
        tmp3 = tmp
      total += tmp3
print(total)
      
