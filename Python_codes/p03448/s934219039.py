a=(int)(input())
b=(int)(input())
c=(int)(input())
n=(int)(input())

count = 0
for i in range(a + 1):
  for j in range(b + 1):
    if (n - (i * 500 + j * 100)) % 50 == 0 and 0 <= (n - (i * 500 + j * 100)) // 50 <= c:
      count += 1
      #print(i, j)
print(count)