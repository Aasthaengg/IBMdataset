def main():
	K,S = map(int,input().split())
	ans = 0
	ListK = [i for i in range(K+1)]
	for x in ListK:
		for y in ListK:
			if 0 <= S - (x + y) <= K:
				ans += 1
	print(ans)

if __name__ == '__main__':
	main()