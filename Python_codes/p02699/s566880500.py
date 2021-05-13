n_sheep, n_wolves = map(int, input().split())

if n_sheep <= n_wolves:
	print('unsafe')
else:
	print('safe')
