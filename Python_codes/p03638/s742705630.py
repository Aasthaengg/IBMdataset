import sys
import copy
sys.setrecursionlimit(10**6)
if sys.platform in (['ios','darwin','win32']):
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]

def main():
	H, W = MAP()
	N = INT()
	A = MAP()
	# print(A)
	
	M = [[0] * W for _ in range(H)]
	# print(M)

	MOVE = [[0,1],[1,0],[0,-1],[-1,0]]

	h, w = 0, 0
	M[0][0] = 1
	A[0] -= 1
	direct = 0
	for i, a in enumerate(A):
		num = i+1
		cnt = a
		if not cnt: continue
		fin = False
		while True:
			for i, move in enumerate(MOVE):
				if i < direct:
					continue
				else:
					direct = 0
					dh, dw = move
				while h+dh < H and h+dh >= 0 and w+dw < W and w+dw >= 0 and M[h+dh][w+dw] == 0:
					h += dh
					w += dw
					M[h][w] = num
					cnt -= 1
					if cnt == 0:
						direct = MOVE.index([dh, dw])
						fin = True
						break
				if fin:	break
			if fin:	break

	for m in M:
		print(' '.join(map(str, m)))

if __name__ == '__main__':
	main()
