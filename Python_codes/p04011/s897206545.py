n = int(input())
k = int(input())
x = int(input())
y = int(input())

# k泊
if (n < k):
    price = n * x
else:
    price = k * x
    # after k+1 
    price += (n-k) * y

print(price)