from sys import stdin 
import math 

def main():

	h, w = map(int, input().split())

	grid = []

	for ind in range(h):
		grid.append(input())


	L = [ [0 for _ in range(w)] for _ in range(h) ]

	L[0][0] = 1

	for h_ind in range(h):
		for w_ind in range(w):
			if grid[h_ind][w_ind] == '.':
				if h_ind - 1 >= 0:
					L[h_ind][w_ind] += L[h_ind - 1][w_ind]
				if w_ind - 1 >= 0:
					L[h_ind][w_ind] +=  L[h_ind][w_ind - 1]


	modulo = int (pow(10, 9) + 7)
	print(L[h - 1][w - 1] % modulo)











if __name__ == '__main__':
	main()



















