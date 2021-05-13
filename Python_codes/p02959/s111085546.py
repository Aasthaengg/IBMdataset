n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
 
sa = sum(a)
 
for i,b in enumerate(b):
	c = min(a[i],b)
	a[i] -= c
	a[i+1] -= min(a[i+1],b-c)
 
print(sa-sum(a))