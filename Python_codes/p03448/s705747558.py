a = int(input())
b = int(input())
c = int(input())
x = int(input())

a = min(x//500, a)+1
b = min(x//100, b)+1
c = min(x//50, c)

cnt = 0

for i in range(a):
  for j in range(b):
    now = x-500*i-100*j
    if now>=0 and now//50 <= c:
      cnt +=1

print(cnt)