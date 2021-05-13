n, k = map(int, input().split())
s = input()

unhappiness = 0
m1, m2 = 0, 0

if s[0] == 'L':
    unhappiness += 1
if s[-1] == 'R':
    unhappiness += 1
i = 0
while i < n and s[i] == 'L':
    i += 1
while i < n:
    h = i
    while i < n and s[i] == 'R':
        i += 1
    if i == n:
        break
    while i < n and s[i] == 'L':
        i += 1
    if h != 0 and i != n:
        m2 += 1
    elif h != 0 or i != n:
        m1 += 1
    unhappiness += 2

if  k <= m2:
    unhappiness -= 2 * k
else:
    unhappiness -= 2 * m2
    k -= m2
    if m1 == 2:
        k -= 1
        unhappiness -= 2
    if k > 0:
        unhappiness = 1
print(n-unhappiness)