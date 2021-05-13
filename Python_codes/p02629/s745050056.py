n = int(input())
str = ''
a = ord('a') - 1
while True:
  z = n % 26 if n % 26 > 0 else 26
  str = chr(a + z) + str 
  n = n // 26 if n % 26 > 0 else n // 26  -1
  if n == 0:
    print(str)
    break