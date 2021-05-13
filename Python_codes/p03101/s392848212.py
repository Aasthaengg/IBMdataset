import re
n = input()
n1 = input()
m = re.search('(\d+)\s(\d+)', n)
m1 = re.search('(\d+)\s(\d+)', n1)
a = int(m.group(1))
b = int(m.group(2))
c = int(m1.group(1))
d = int(m1.group(2))
ab = a * b
cd = c * b + d * (a - c)
print(ab - cd)
