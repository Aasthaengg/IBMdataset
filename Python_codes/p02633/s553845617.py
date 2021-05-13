x = int(input())
a = 1
for i in [2,2,2,3,3,5]:
  if x%i == 0:
    a *= i
    x //= i
print(360//a)