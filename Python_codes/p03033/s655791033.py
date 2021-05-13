import sys
from operator import itemgetter
def main():
	inputs = sys.stdin.readline
	N, Q= map(int,inputs().split())
	E = [None]*2*N
	for n in range(N):
		a,b,c = map(int,inputs().split())
		E[2*n] = (a - c, 1, c)
		E[2*n + 1] = (b - c, -1, c)
	E.sort(key=itemgetter(0))
	tuple(tuple(E))
	mini = 1000000001
	kouho = {1000000001}
	my_add = kouho.add
	my_discard = kouho.discard
	q = 0
	d = int(inputs())
	flag = False
	cont = False
	for e in E:
		while e[0] > d:
			if cont == True:
				print(mini-(mini//1000000001)*1000000002)
			else:
				mini = min(kouho)
				print(mini-(mini//1000000001)*1000000002)
			cont = True
			q = q + 1
			if q > Q-1:
				flag = True
				break
			d = int(inputs())
		if flag == True:
			break
		if e[1] == 1:
			my_add(e[2])
			if mini > e[2]:
				mini = e[2]
		elif e[1] == -1:
			my_discard(e[2])
			if mini == e[2]:
				cont = False
	for t in [None]*(Q-q):
		print(-1)
main()