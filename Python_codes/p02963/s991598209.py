S = int(input())

x2 = 10**9
x3 = (x2 - S%x2) % x2
y3 = (S + x3) // x2

print('0 0 {} 1 {} {}'.format(x2,x3,y3))