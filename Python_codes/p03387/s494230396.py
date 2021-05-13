# no matter what in every operation u will be adding two to the sum of all the numbers
# check when 2*i is divisible by 3 and each no should be greater than the maximum
def main():
	a, b , c = map(int , input().split())
	if a==b and b==c:
		print(0)
	else:
		tot=0
		tot = tot+(a+b+c)
		mx = max(a, max(b, c))
		i = 0
		f=0
		while f==0:
			if((tot+2*i)%3==0):
				p = ((tot+2*i))//3
				if p>=mx:
					f=1
			i = i+1
		print(i-1)
if __name__=="__main__":
	main()