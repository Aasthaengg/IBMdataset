a,b,c=map(int,input().split())
if a%c==0:
	l=a 
else:
	l=(a//c+1)*c 
if b%c==0:
	u=b 
else:
	u=(b//c)*c 
#print(l,u)
print(max(0,(u-l)//c+1))