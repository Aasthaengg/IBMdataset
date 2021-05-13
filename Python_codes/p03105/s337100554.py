import re
n = input()
m = re.search('(\d+)\s(\d+)\s(\d+)', n)
a = int(m.group(1))
b = int(m.group(2))
c = int(m.group(3))
i = b // a
if c <= i:
    print(c)
else:
    print(i)
