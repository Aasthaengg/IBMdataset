N = int(input())
flg = 0

for i in range(N//7+1):
    for j in range(N//4+1):
        money = 7*i + 4*j
        if money == N:
            flg = 1
            break
      
if flg == 1:
  print('Yes')
else:
  print('No')
