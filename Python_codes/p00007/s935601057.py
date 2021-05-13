a = input()
ret = 100000

while 0<a:
	ret *= 1.05
	if(ret%1000):
		ret = int((ret//1000+1)*1000)
	a -= 1
	
print ret