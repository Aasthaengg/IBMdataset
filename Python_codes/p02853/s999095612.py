x,y = map(int,input().split())
m = 0

if x == 3:
    m += 100000

if x == 2:
    m += 200000

if x == 1:
    m += 300000

if y == 3:
    m += 100000

if y == 2:
    m += 200000

if y == 1:
    m += 300000

if m == 600000:
    m += 400000

print(m)