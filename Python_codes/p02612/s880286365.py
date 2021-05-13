N = int(input())

if N % 1000 == 0:
  a = N // 1000
else:
  a = N //1000 + 1
  
print(a*1000 -N)