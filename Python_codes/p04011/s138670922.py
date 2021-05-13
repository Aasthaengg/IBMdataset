n = int(input())
k = int(input())
x = int(input())
y = int(input())

price = 0

for i in range(1,n+1):
    if i < k+1:
        price += x
    else:
        price += y

print(price)