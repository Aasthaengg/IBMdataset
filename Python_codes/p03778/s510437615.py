w, a, b = map(int, input().split())
al = a + w
bl = b + w
r = 0
if b >= a and b <= al:
	r = 0
elif bl >= a and bl <= al:
	r = 0
else:
	r = b - al if b > al else a - bl
print(r)