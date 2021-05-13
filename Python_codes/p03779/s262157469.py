from math import sqrt
x = int(input())

if (sqrt(1 + 8*x) - 1)%2 == 0:
    x_ = (sqrt(1 + 8*x) - 1)//2 
else:
    x_ = (sqrt(1 + 8*x) - 1)//2 +1

print(int(min(x, x_)))