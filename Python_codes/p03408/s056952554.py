def calc(blue, red):
	lst = []
	
	for ch in blue:
		if ch in red:
			lst.append(blue[ch] - red[ch])
		else:
			lst.append(blue[ch])

	return max(lst)


def main():
	N = int(input())
	blue = {}

	for _ in range(N):
		ch = input()
		if ch in blue:
			blue[ch] += 1
		else:
			blue[ch] = 1

	M = int(input())
	red = {}

	for _ in range(M):
		ch = input()
		if ch in red:
			red[ch] += 1
		else:
			red[ch] = 1

	value = calc(blue, red)

	if value >= 0:
		print(value)
	else:
		print(0)	

  
if __name__ == "__main__":
  	main()