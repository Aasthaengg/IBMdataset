a, b = input().split()
s = int(a+b)
n = 0
flg = False
while n*n <= s:
  if n*n == s:
    flg = True
  n += 1
  
if flg:
  print("Yes")
else:
  print("No")