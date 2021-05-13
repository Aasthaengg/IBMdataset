import sys
INF = (sys.maxint)/3

def MaximumProfit(R_list):
	minR = INF
	maxD = -INF
	for R in R_list:
		maxD = max(maxD, R - minR)
		minR = min(minR, R)
	return maxD

def main():
	n = input()
	R_list = []
	for i in range(n):
		R_list.append(input())
	print MaximumProfit(R_list)

if __name__ == '__main__':
	main()