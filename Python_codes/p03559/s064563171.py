# a[i]<b[j]<c[k]
# iterate over b and find the lower bound and upper bound in a and c respectively
from bisect import bisect_left , bisect_right
def main():
	n = int(input())
	a = list(map(int , input().split()))
	b = list(map(int, input().split()))
	c = list(map(int ,input().split()))
	a.sort()
	b.sort()
	c.sort()
	ans=0
	for i in b:
		k = bisect_left(a,i)
		l = bisect_right(c,i)
		ans = ans+(k*(n-l))
	print(ans)
if __name__=="__main__":
	main()