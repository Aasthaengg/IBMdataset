import sys
readline = sys.stdin.readline
def main():
	limit = 10 ** 4
	n = int(input())
	a = []
	for _ in range(n):
		a.append(tuple(map(int,input().split())))
	a = tuple(a)

	play = [0 for _ in range(n)]
	flag = [True for _ in range(n)]
	count = 0
	ans = 0
	while True:
		break_flag = True
		for i in range(n):
			if flag[i]:
				num = a[i][play[i]]-1
				if flag[num] and a[num][play[num]]-1 == i:
					play[num] += 1
					play[i] += 1
					flag[num] = False
					flag[i] = False
					break_flag = False
					count += 1
		if break_flag:
			print(-1)
			sys.exit()
		ans += 1

		if count == n*(n-1)//2:
			break
		if ans > limit:
			print(n*(n-1)//2)
			sys.exit()
		for i in range(n):
			if play[i] < n-1:
				flag[i] = True
			else:
				flag[i] = False

	if ans == 0:
		print(-1)
	else:
		print(ans)
if __name__ == '__main__':
	main()