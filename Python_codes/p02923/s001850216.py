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
h = intl()

cnt = 0
ans = 0
for i in range(1,n):
	if h[i] <= h[i-1] :
		cnt += 1
	else:
		cnt = 0
	ans = max(ans, cnt)
print(ans)
