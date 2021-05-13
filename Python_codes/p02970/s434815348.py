m = input()
m = m.split(' ')
n = int(m[0])
d = int(m[1])
s = 0
q = 0
while s < n:
    s += (d * 2 + 1)
    q += 1

print(q)