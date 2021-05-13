import sys,collections as cl
Max = sys.maxsize
def l():
	return list(map(int,input().split()))
def m():
	return map(int,input().split())
def s(x):
	a = []
	aa = x[i]
	su = 1
	for i in range(len(x)-1):
		if aa == x[i+1]:
			a.append([aa,su])
			aa = x[i+1]
			su = 1
		else:
			su += 1
	a.append([aa,su])
	return a
def jo(x):
	return " ".join(map(str,x))

n,a,b = m()

k = abs(a-b)
if k == 1:
	print("Borys")
else:
	if k % 2 == 0:
		print("Alice")
	else:
		print("Borys")


