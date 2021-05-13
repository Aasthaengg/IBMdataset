n = int(input())
if n == 0:
  print(0)
  exit(0)
for k in range(100):
    if -2*pow(4,k) +2 < 3*n < pow(4,k) - 1:
        break
l = 2*k

delta = n - (-2*(pow(2,l)-1)//3)

var = delta ^ (2*(pow(2,l)-1)//3)

ans = ''
while var > 0:
    if var&1:
        ans ='1'+ans
    else:
        ans ='0'+ans
    var = var >> 1
print(ans)
