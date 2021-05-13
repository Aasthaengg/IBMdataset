import functools as fun

def main():
	N, K = map(int, [input() for _ in range(2)])

	print( fun.reduce(lambda x,_: min(x*2, x+K), range(1, N+2)) )
	return

main()

