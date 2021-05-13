a, b = [int(i) for i in input().split()]

d = a // b
r = a % b
f = a / b

print('%d %d %.10f' %(d, r, f))