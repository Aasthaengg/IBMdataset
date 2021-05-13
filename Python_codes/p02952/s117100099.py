n = input()
ans = 0
for i in range(0,len(n)):
  if i % 2 == 1:
    max_num = 10 ** i 
    min_num = 10 ** (i-1)
    ans +=  max_num - min_num
if len(n) % 2 == 1:
  ans += int(n) - (10 ** (len(n)-1) - 1)
print(ans)