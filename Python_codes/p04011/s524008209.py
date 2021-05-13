
def main():
	n = int(input())
	k = int(input())
	x = int(input())
	y = int(input())
	if n<=k:
		print(n*x)
	else:
		ans = 0
		ans = ans+k*x
		n = n-k
		ans = ans+n*y
		print(ans)
if __name__=="__main__":
	main()