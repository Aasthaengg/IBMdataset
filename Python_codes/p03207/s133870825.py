n = int(input())
price = []
for i in range(n):
    p = int(input())
    price.append(p)
    
total_price = sum(price) - max(price)//2
print(total_price)