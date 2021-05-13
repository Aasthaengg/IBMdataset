# source wikipedia negabinary 
def main():
	n = int(input())
	ans = ""
	while n!=0:
		rem = n%(-2)
		n= n//(-2)
		if rem<0:
			rem = rem+2
			n = n+1
		ans = ans + chr(rem + ord('0'))
	if ans =="":
		print(0)
		exit()
	print(ans[::-1])
if __name__ =="__main__":
	main()