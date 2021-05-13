s = int(input())
m = 0
t = 0
for i in range(s):
    m, n = input().split()
    m = float(m)
    if n == 'JPY':
        t += m
    else:
        t += 380000*m
print(t)