N = int(input())
K = int(input())
X = int(input())
Y = int(input())
price = 0
for i in range(1,N+1):
    if i <= K:
        price = price + X
    else:
        price = price + Y
print(price)