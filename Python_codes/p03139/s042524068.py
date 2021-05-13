
n , a, b = map(int, input().split())
n = int(n)
a = int(a)
b = int(b)


if (a > b ) :
	mx_x = b
else:
	mx_x = a

if ((a+b - n)<0):
	mx_y = 0
else:
	mx_y = a+b-n

print(str(mx_x) + ' ' + str(mx_y))




