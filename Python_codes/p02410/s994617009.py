n, m = map(int, raw_input().split());
i = 0
ar = [0] * n
vc = [0] * m
while i < n:
	ar[i] = map(int, raw_input().split());
	i += 1
i = 0
while i < m:
	vc[i] = input();
	i += 1
for el in ar:
	ans = 0
	for el2, el3 in zip(vc, el):
		ans += el2 * el3
	print ans