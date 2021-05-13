from sys import stdin
from math import ceil
def main():
	readline=stdin.readline
	N=int(readline())
	a=list(map(int,readline().split()))
	b=list(map(int,readline().split()))

	count=0
	for i in range(N):  #一旦、任意のiについてa_iをb_iよりも大きくする。
		if a[i]<b[i]:   #その時の回数をcountとする。
			c=ceil((b[i]-a[i])/2)
			count+=c
			a[i]+=2*c

	for i in range(N):  #count以内の回数でbも大きくしていく。
		if b[i]<a[i]:   #上の手順後にa<=bならa_i<b_iのiについて
			d=a[i]-b[i] #a_iとb_iを同時に増やしていけばa=bにすることができ、
			b[i]+=d     #a>bなら逆転不可能でa=bにすることはできない。
			count-=d

	if count>=0:
		print("Yes")
	else:
		print("No")

if __name__=="__main__":
	main()