a,b = input().split()
a = int(a)
b = b[:-3] + b[-2:]
b = int(b)
print(a*b//100)