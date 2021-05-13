N = int(input()) 
num = N // 11
res = num * 2
k = num * 11
if 0< N % 11 <= 6:
  res +=  1
elif 7<= N % 11 <= 10:
  res +=  2
else:
  pass  
print(res)