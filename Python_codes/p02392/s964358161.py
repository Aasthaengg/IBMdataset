i = j = k = 0
n = ''
m = ''
l = ''

line = input()

while line[i] != ' ':
    n = n + line[i]
    i += 1

i += 1
while line[i] != ' ':
    l = l + line[i]
    i += 1

while i < len(line):
    m = m + line[i]
    i += 1
    
n = int(n)
l = int(l)
m = int(m)

if n < l and l < m:
    print("Yes")
else:
    print("No")