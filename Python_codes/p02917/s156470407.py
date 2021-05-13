n = int(input())

b = list(map(int, input().split()))
a=[0]*n
a[0]=b[0]
a[n-1]=b[n-2]

for i in range(1, n-1):
	if b[i]>=b[i-1]:
		a[i]=b[i-1]
	else:
		a[i]=b[i]
s = 0
for i in range(n):
	s += a[i]
	
print(s)