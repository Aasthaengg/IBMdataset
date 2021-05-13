a,b,c = map(int,raw_input().split())

count = 0
for n in range(a,b+1):
	if c % a == 0:
		count += 1
	a += 1

print('{0}'.format(count))