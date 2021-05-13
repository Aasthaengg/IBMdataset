from sys import stdin
from math import ceil
def main():
	readline=stdin.readline
	N=int(readline())
	a=list(map(int,readline().split()))
	b=list(map(int,readline().split()))
	a_count=0
	s=sum(b)-sum(a)

	for i in range(N):
		if a[i]<b[i]:
			a_count+=ceil((b[i]-a[i])/2)

	if a_count<=s:
		print("Yes")
	else:
		print("No")

if __name__=="__main__":
	main()