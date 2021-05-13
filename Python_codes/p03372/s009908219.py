from itertools import accumulate as f

def main():
	n, c, *L = map(int, open(0).read().split())
	acc = [a - x for x, a in zip(L[::2], f(L[1::2]))]
	acc_max = list(f(acc, max))[::-1]
	R = L[::-1]
	rev = [a - (c - x) for x, a in zip(R[1::2], f(R[::2]))]
	rev_max = list(f(rev, max))[::-1]
	p = max([a - b + d for a, b, d in zip(acc, L[::2], rev_max[1:])]+[0])
	q = max([a - (c - b) + d for a, b, d in zip(rev, R[1::2], acc_max[1:])]+[0])
	r = max(0, acc_max[0], rev_max[0])
	print(max(p, q, r))

if __name__ == "__main__":
	main()
