n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

 
sm = sum(a)
for i in range(n):
	c = min(a[i],b[i])
	a[i] -= c
	a[i+1] -= min(a[i+1],b[i]-c)
	
print(sm-sum(a))