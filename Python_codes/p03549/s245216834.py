import math
n,m = map(int, input().split())

ans = 0

time = (n-m) * 100 + m * 1900
for i in range(1, 1000000):
  ans += pow(1-pow(0.5,m),i-1) * pow(0.5,m) * time * i

temp = math.ceil(ans)
if str(temp)[-1] == "1":
  print(temp - 1)
elif str(temp)[-1] == "9":
  print(temp + 1)
else:
  print(temp)