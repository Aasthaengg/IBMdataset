s = input().split()

a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

x = c - a
y = d - b

print(c - y, end=' ')
print(d + x, end=' ')
print(a - y, end=' ')
print(b + x)