
# find the cluster of LLLLL....... and RRRRR....
# Reversing these cluster increases happiness by 2
# either the leftmost or the rightmost will remain unhappy forever can't help :(
def main():
	n , k = map(int, input().split())
	s = input()
	uh=0
	for i in range(0 , len(s)-1):
		if s[i]!=s[i+1]:
			uh=uh+1
	hp = n-1 - max(uh-2*k , 0)
	print(hp)


if __name__=="__main__":
	main()