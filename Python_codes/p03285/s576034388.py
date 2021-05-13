N=int(input())
for i in range(N//4+1):
  tmp = N - 4*i
  if tmp >= 0 and tmp % 7 == 0:
    print('Yes')
    exit()
print('No')