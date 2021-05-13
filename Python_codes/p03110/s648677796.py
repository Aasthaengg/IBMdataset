n = int(input())
a = [ list(input().split()) for _ in range(n) ]
#a = [['10','JPY'],['0.00001','BTC']]

yen = 0
btc = 0
for i,j in a:
  if j == 'JPY':
    yen += int(i)
  else:
    btc += float(i)

print(yen + btc * 380000)