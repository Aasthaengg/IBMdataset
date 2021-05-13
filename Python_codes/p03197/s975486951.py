# if any tree contains an odd no of table then first is the winner
# First strategy is to make a tree with odd no of apples
# second strategy is to make a tree with even no of apples
# if the tree doesn't contain any odd apples when first takes an apples he will make it odd
# second would try to make it even by taking one apple from that tree
def main():
	n = int(input())
	ans =0
	f=0
	for i in range(0 , n):
		t = int(input())
		if t%2!=0:
			f=1
	if f==1:
		print("first")
	else:
		print("second")
if __name__=="__main__":
	main()