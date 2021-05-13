n = int(input())
k = int(input())
x = int(input())
y = int(input())

o = n - k

sum = 0
if o > 0:
    sum += k * x
    sum += o * y
else:
    sum += n * x

print(sum)