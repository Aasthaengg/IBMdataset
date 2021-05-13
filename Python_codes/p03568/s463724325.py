def main():
	n = int(input())
	arr =list(map(int , input().split()))
	ans = 0
	allseq = 1
	bad = 1
	# find the no of sequence which has product of all numbers odd
	# subtract the total no of sequence  
	for i in range(0 , n):
		if arr[i]%2==0:
			bad = bad*2# b can take value arr[i]-1 or arr[i]+1
		else:
			bad = bad*1# b can take value only arr[i]
		allseq = allseq*3# total no of elements
	print(allseq-bad)
if __name__=="__main__":
	main()