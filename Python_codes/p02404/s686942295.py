if __name__ == "__main__":
	lis = []
	while True:
		a, b = map( int, input().split() )
		if a == b == 0:
			break
		lis.append([a,b])
	for i in lis:
		print('#'*i[1])
		for j in range(i[0]-2):
			print('#'+'.'*(i[1]-2)+'#')
		print('#'*i[1])
		print()