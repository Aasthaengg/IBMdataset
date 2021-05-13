x = int(input())
n = 100
count = 0
while(x > n):
  n = (n * 101)//100
  count += 1
print(count)