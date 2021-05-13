i = j = 0
n = ''
m = ''


line = input()

while line[i] != ' ':
    n = n + line[i]
    i += 1
    
while i < len(line):
    m = m + line[i]
    i += 1
    
n = int(n)
m = int(m)

if n == m:
    print("a == b")

if n > m:
    print("a > b")

if n < m:
    print("a < b")