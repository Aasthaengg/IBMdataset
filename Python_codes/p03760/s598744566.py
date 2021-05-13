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

o = s()
e = s()

ans = ""
for i in range( len(o)+len(e) ):
	if i%2 == 0:
		ans += o[i//2]
	else:
		ans += e[i//2]
print(ans)