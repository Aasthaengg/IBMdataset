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
ans = [0]*n
for i in range(m):
	a,b = i2()
	ans[a-1] += 1
	ans[b-1] += 1 
	
for i in range(n):
	print(ans[i])

