a, b, c = map(int, input().split())
temp = a
a = b
b = temp
temp = a
a = c
c = temp

print('{} {} {}'.format(a,b,c))