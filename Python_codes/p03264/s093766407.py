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

k = i()
ans = 0
ls = list(int(k) for k in range(1,k+1))
for i in range(k):
	ans += ls[i]//2
print(ans)