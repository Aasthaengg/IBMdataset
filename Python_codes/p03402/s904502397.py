import math
def main():
	A, B = map(int,input().split())
	K = 50
	ans = [["#" if i < K else "." for _ in range(2*K)] for i in range(2*K)]
	num_w = 0
	num_b = 0
	for i in range(A-1):
		k = (i*2//(2*K))*2
		l = (i*2)%(2*K)
		ans[k][l] = "."

	for i in range(B-1):
		k = (i*2//(2*K))*2
		l = (i*2)%(2*K)
		ans[K+1+k][l] = "#"

	l1 = str(2*K) + " " + str(2*K)
	print(l1)
	for i in range(2*K):
		this_ans = ""
		for j in range(2*K):
			this_ans += ans[i][j]
		print(this_ans)


if __name__ == '__main__':
    main()