def solve():
	a, b = map(int, input().split())
	if (a + b) % 2 == 1:
		return "IMPOSSIBLE"
	else:
		return int((a + b) / 2)
		
		
if __name__ == "__main__":
	print(solve())