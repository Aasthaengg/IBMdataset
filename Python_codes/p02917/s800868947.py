def i():
	return int(input())
def i2():
	return map(int,input().split())
def s():
	return str(input())
def l():
	return list(input())
def intl():
	return list(int(k) for k in input().split())

n = i()
b = intl()

a = b[0] + b[-1]
for i in range(n-2):
	a += min( b[i], b[i+1] )
print(a)