n = int(input())

min = n

def digits_sum(x):
    _x = 0
    while x > 0:
        _x += x % 10
        x //= 10
    
    return _x


for i in range(2, n):
    a = i
    b = n - i
    if digits_sum(a) + digits_sum(b) < min:
        min = digits_sum(a) + digits_sum(b)

print(min)