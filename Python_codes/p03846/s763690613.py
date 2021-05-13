import collections
n = int(input())
a = list(map(int, input().split()))
mod = 10**9+7
c = collections.Counter(a)
cl = ""
if n%2 == 1:
	cl = "odd"
else:
	cl = "even"
ans = 0
flg = True
if cl == "odd":
	for i in c:
		if i%2 == 1:
			flg = False
		if i == 0:
			if c[i] != 1:
				flg = False
		else:
			if c[i] != 2:
				flg = False
else:
	for i in c:
		if i%2 == 2:
			flg = False
		if c[i] != 2:
			flg = False
if not (flg):
	print (ans)
	exit()
ans = 2**(n//2)%mod
print (ans)