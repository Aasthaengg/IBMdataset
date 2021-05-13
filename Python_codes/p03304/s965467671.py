# your code goes here
#N=int(input())
#l = list(map(int,input().split()))
n,m,d = map(int,input().split())
k = abs(n-2*d-1)+1
if n > d + 1:
	x = n + k
else:
	x = 2
if d == 0:
	x = n
f = x/n/n
if n == 0 :
	print(0)
else:

		print((m-1)*x/n/n)
	# your code goes here