import re
a = input()
b = input()
c = re.search('(\d+)\s(\d+)', a)
d = int(c.group(1))
e = int(c.group(2))
result = ''
for n in range(d):
    if n == e - 1:
        r = str(b[n]).lower()
        result += r
    else:
        result += b[n]
print(result)
