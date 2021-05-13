import math

def some():
    n = int(input())
    y = int(math.sqrt(n))
    data = [(i+n//i)-2 for i in range(y, 0, -1) if n%i==0]
    print(min(data))

some()