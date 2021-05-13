N = int(input())
ans = 0
for i in range(4):
 a = N%10
 if a==2:
  ans = ans+ 1
 N /= 10
 N = int(N)
print(ans)
