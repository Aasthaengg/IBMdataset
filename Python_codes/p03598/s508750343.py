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
  
n=i()
k=i()
x=intl()
a=0
for i in range(n):
	a+=min(2*x[i],2*abs(x[i]-k))
print(a)