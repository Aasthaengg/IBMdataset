x = input().split()
a = int(x[0])
b = int(x[1])
l = [a+b, a-b, a*b]
print(sorted(l, reverse=True)[0])