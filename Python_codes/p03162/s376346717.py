from sys import stdin 

def main():

	n = int(input())

	h_vals = []

	for lines in range(n):
		h = list(map(int, input().split()))
		h_vals.append(h)

	L = [ [0 for _ in range(n + 1)] for _ in range(3) ]


	for cur_day in range(1, n + 1):
		for val in range(3):
			cur_max = 0
			other_vals = [0, 1, 2]
			other_vals.remove(val)
			for other_val in other_vals:
				cur_max = max(L[other_val][cur_day - 1] + h_vals[cur_day - 1][other_val], cur_max)
			L[val][cur_day] = cur_max

	print(max(L[0][n], L[1][n], L[2][n]))









if __name__ == '__main__':
	main()

