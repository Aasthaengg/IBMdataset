
def main():
	n = int(input())
	k = n//50
	rem = n%50
	arr = [0 for i in range(50)]
	for i in range(0 , 50):
		arr[i]=i
	for i in range(0 , 50):
		arr[i]=arr[i]+k
	while rem>0:
		for i in range(0 , 50):
			if arr[i]==k:
				arr[i]=arr[i]+50 # after k operation this element becomes 0 next operation it becomes 
			else:				# negative so we just need to add 50 so that it become 49 still smaller than 50
				arr[i]=arr[i]-1
		rem=rem-1
	print(50)
	print(*arr)
if __name__ == "__main__":
	main()	