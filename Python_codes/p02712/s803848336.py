n = int(input())
b = int(n / 3)
c = int(n / 5)
d = int(n / 15)
a = (n * (n + 1) / 2) - (b * (b + 1) / 2) * 3 - (c * (c + 1) / 2) * 5 + (d * (d + 1)/ 2) * 15
print(int(a))