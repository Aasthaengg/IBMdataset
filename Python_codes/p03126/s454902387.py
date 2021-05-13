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

n,m = i2()
ls = []
for _ in range(n):
	a = intl()
	a = a[1:]
	ls.append(a)

for i in range(n-1):
	tmp = []
	for j in ls[i]:
		for k in ls[i+1]:
			if j == k:
				tmp.append(j)
	ls[i+1] = tmp

print( len(ls[-1]) )