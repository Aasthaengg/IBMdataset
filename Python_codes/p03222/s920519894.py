#ライブラリインポート
from collections import defaultdict
import copy

#入力受け取り
def getlist():
	return list(map(int, input().split()))

INF = 10 ** 9 + 7

#処理内容
def main():
	H, W, K = getlist()
	A = [0] * W
	A[0] = 1
	if W == 1:
		print(1)
	else:		
		for i in range(H):
			B = [0] * W
			for j in range(1 << (W - 1)):
				output = [0] * (W - 1)
				for k in range(W - 1):
					if ((j >> k) & 1) == 1:
						output[k] = 1
				judge = "Yes"
				for k in range(W - 2):
					if output[k] == 1 and output[k + 1] == 1:
						judge = "No"
				if judge == "Yes":
					if output[0] == 1:
						B[0] += A[1]
					else:
						B[0] += A[0]
					for k in range(1, W - 1):
						if output[k - 1] == 1:
							B[k] += A[k - 1]
						elif output[k] == 1:
							B[k] += A[k + 1]
						else:
							B[k] += A[k]
					if output[W - 2] == 1:
						B[W - 1] += A[W - 2]
					else:
						B[W - 1] += A[W - 1]

			for i in range(W):
				B[i] %= INF
			A = copy.deepcopy(B)
		print(A[K - 1] % INF)
	
if __name__ == '__main__':
	main()