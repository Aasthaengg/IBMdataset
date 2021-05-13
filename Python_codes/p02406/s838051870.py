n = int(input())

r = ''
for i in range(1, n+1):
    x = i
    if x % 3 == 0:
        r += ' '+str(x)
        continue
    while x > 0 and x % 10 != 3:
        x = x // 10
    if x % 10 == 3:
        r += ' '+str(i)
print(r)