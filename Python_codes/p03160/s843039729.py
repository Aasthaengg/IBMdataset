from sys import stdin 

def main():

	n = int(input())

	h = list(map(int, input().split()))

	#print(n, h)

	L = [0 for _ in range(n)]

	L[0] = 0
	L[1] = abs(h[1] - h[0])

	for ind in range(2, n):
		L[ind] = min(L[ind - 1] + abs(h[ind] - h[ind - 1]), L[ind - 2] + 
			abs(h[ind] - h[ind - 2]))

	print(L[-1])





if __name__ == '__main__':
	main()



















