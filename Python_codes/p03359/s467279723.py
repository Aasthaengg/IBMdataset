
def main():
	line = input()
	vector = [int(x) for x in line.split()]
	a = vector[0]
	b = vector[1]
	if a <= b:
		print(a)
	else:
		print(a - 1)
 
 
 
if __name__ == "__main__":
	main()