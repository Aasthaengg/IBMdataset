n = int(input())
l = 0
r = n-1

def get(i):
	print(i)
	s = input()
	if s == 'Vacant':
		exit()
	return s


def kind(i):
	return (i%2) ^ (get(i)=='Male')


kl = kind(l)
kr = kind(r)

while True:
	m = (l+r)//2
	km = kind(m)
	if km==kl:
		l, kl = m, km
	else:
		r, kr = m, km

