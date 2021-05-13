n = int(input())
a = n // 100
b = a * 100 + a * 10 + a
if(n > b):
  ans = (a + 1) * 100 + (a + 1) * 10 + (a + 1)

else:
  ans = a * 100 + a * 10 + a
print(ans)