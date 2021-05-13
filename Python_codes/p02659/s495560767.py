a, b = input().split()
a = int(a)
b1, b2 = map(int, b.split('.'))
b100 = b1*100 + b2
      
print(a*b100//100)