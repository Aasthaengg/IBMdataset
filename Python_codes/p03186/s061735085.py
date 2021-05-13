a,b,c = map(int, input().split())

num = min(b, c)
num2 = 0
c -= num
if num > 0:
    num2 = min(c, a)
c -= num2

sum = num*2 + num2
b -= num
if b > 0:
    sum += b
if c > 0:
    sum += 1

print(sum)