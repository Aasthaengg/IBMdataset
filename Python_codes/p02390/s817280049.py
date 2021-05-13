sum = int(input())
h = sum // 60**2
m = (sum % 60**2) // 60
s = sum % 60
print(h, m, s, sep=':')
