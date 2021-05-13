import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

a = b = None

for i, x in enumerate(itertools.permutations(range(1, n+1), n)):
	if p == x:
		a = i
		if b:
			break
		
	if q == x:
		b = i
		if a:
			break
			
print(abs(a - b))
