import sys
from collections import deque,defaultdict

I=sys.stdin.readline

def ii():
	return int(I().strip())
def li():
	return list(map(int,I().strip().split()))

def mi():
	return map(int,I().strip().split())


def main():
	ans=""
	n,k=mi()
	arr=li()
	a=0
	for i in range(n-k):
		tmp=arr[k+i]
		if tmp>arr[a]:
			ans+="Yes\n"
		else:
			ans+="No\n"
		a+=1
	print(ans)








		


		










		






if __name__ == '__main__':
	main()