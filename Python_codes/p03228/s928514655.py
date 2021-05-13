a, b, k = map(int, input().split())

for i in range(k):
	if i%2==0:
		if a%2==1:
			a-=1
		a = a/2
		b = b+a
	if i%2==1:
		if b%2==1:
			b-=1
		b = b/2
		a = b+a

print("{} {}".format(int(a), int(b)))