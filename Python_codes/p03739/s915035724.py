def main():
	n = int(input())
	a = list(map(int, input().split()))

	ans_v1 = 0
	ans_v2 = 0
	a_sum_v1 = 0
	a_sum_v2 = 0

	for i in range(0, n):
		if i % 2 == 0: # 0,2,4...番目までの和を正
			if a_sum_v1 + a[i] < 1:
				ans_v1 += 1 - a_sum_v1 - a[i]
				a_sum_v1 = 1
			else:
				a_sum_v1 += a[i]
		else:          # 1,3,5...番目までの和を負
			if a_sum_v1 + a[i] > -1:
				ans_v1 += 1 + a_sum_v1 + a[i]
				a_sum_v1 = -1
			else:
				a_sum_v1 += a[i]
	
	for i in range(0, n):
		if i % 2 == 0: # 0,2,4...番目までの和を負
			if a_sum_v2 + a[i] > -1:
				ans_v2 += 1 + a_sum_v2 + a[i]
				a_sum_v2 = -1
			else:
				a_sum_v2 += a[i]
		else:          # 1,3,5...番目までの和を正
			if a_sum_v2 + a[i] < 1:
				ans_v2 += 1 - a_sum_v2 - a[i]
				a_sum_v2 = 1
			else:
				a_sum_v2 += a[i]

	print(min(ans_v1, ans_v2))

 
if __name__ == "__main__":
  	main()