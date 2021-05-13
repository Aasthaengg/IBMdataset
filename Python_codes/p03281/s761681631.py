def divide_num(n):
  ans = 0
  for i in range(1,n+1):
    if n%i == 0:
      ans+=1
  return ans
n = int(input())
res = 0
for i in range(1,n+1):
  d = divide_num(i)
  if d == 8 and i%2 ==1:
    res +=1
print(res)