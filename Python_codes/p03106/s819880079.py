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

a,b,k = i2()
ans = []*100
for i in range( 1,min(a,b)+1 ):
	if a%i==0 and b%i==0:
		ans.append(i)
print(ans[-k])