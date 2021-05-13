(a,b) = [int(x) for x in input().rstrip().split()]

d = a // b
r = a % b
f = a / b

print('{0} {1} {2:.8f}'.format(d,r,f))