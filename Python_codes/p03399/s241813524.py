a = int(input())
b = int(input())
c = int(input())
d = int(input())

res = 0
if a > b:
    res += b
else:
    res += a

if c > d:
    res += d
else:
    res += c

print(res)