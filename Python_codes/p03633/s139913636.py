import sys
import math

if __name__ == "__main__":
	n = int(input())
	lst = []
	for _ in range(n):
		lst.append(int(input()))
	q = lst[0]
	for x in range(1, n):
		q = (q*lst[x])//math.gcd(lst[x], q)
	print(q)