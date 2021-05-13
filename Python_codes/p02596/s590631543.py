k = int(input())
num = 7

if k == 1 or k == 7:
  print(1)
  exit()

if k%2==0:
  print(-1)
  exit()
for i in range(1, k + 1):
    num = num * 10 + 7
    if num % k == 0:
        print(i + 1)
        exit()
    else:
        num %= k
        
print(-1)
exit()