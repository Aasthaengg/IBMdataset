aa, bb = input().split()
a = int(aa)
b0,b1 = bb.split(".")
b = int(b0 + b1)
print(a * b//100)