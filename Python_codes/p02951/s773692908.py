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
  
a,b,c=i2()
if a>=b+c:
	print(0)
elif a<b+c and a>=b:
	print(c-a+b)
elif a<b:
	print(c)