import itertools as itr

def main():
	N, M, Q = list(map(int, input().split()))
	LR      = [map(int, input().split()) for _ in range(M)]
	pq      = [map(int, input().split()) for _ in range(Q)]

	cnt = [[0 for _ in range(N+10)] for _ in range(N+10)]
	for L, R in LR:
		cnt[L][R] += 1
	
	for i, j in itr.product(range(N+1), repeat = 2):
		cnt[i+1][j] += cnt[i][j]
	for i, j in itr.product(range(N+1), repeat = 2):
		cnt[i][j+1] += cnt[i][j]

	for p, q in pq:
		print( cnt[q][q] - cnt[p-1][q] - cnt[q][p-1] + cnt[p-1][p-1] )

	return


main()

