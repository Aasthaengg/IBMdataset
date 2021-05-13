num = []
n = int(input())
while n != 0:
  num.append(n % 10)
  n //= 10
num.reverse()

count = 0

for i in range(len(num)):
    if num[i] == 2:
        count = count + 1

print(count)