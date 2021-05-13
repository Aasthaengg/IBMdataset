def gcd(a,b):
	if(a==0 or b==0):
		return a+b
	return gcd(b,a%b)
n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
val=0
for c in l:
	val = gcd(val,c)
if(k%val==0 and k<=max(l)):
	print("POSSIBLE")
else:
	print("IMPOSSIBLE")