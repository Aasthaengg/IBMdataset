def main():
	c = []
	
	for _ in range(3):
		c.append(list(map(int, input().split())))

	a = [0] * 3
	b = [0] * 3

	for i in range(3):
		b[i] = c[0][i] - a[0]

	for i in range(1, 3):
		a[i] = c[i][0] - b[0]
	
	is_able = True

	for i in range(3):
		for j in range(3):
			if a[i] + b[j] != c[i][j]:
				is_able = False
				break

	if is_able:
		print("Yes")
	else:
		print("No")

  
if __name__ == "__main__":
  	main()