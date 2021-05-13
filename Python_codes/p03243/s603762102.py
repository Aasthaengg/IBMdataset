s = input()
n = int(s)

m = []

y = n
while y > 0:
    z = y % 10
    m.append(z)
    y = int(y / 10)
    
p = m[len(m) - 1]


max_num = 0
for i in range(len(m)):
    max_num = max(max_num, m[i])

if p < max_num:
    p += 1


for i in range(len(m)):
    m[i] = p
    print(m[i], end='')

print('')