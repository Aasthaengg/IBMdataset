x = int(input())
n = 100
y = 0

while n < x:
    n = (n*101)//100
    y += 1
print(y)