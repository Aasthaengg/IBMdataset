x, a, b = map(int, input().split())
e = b - a
r = 'safe'
if e > x:
	r = 'dangerous'
elif e < 1:
	r = 'delicious'
print(r)