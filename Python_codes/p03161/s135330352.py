II = lambda: int(input())
SI = lambda: input()
LI = lambda: list(map(int,input().split()))
MI = lambda: map(int,input().split())
n,k = MI()
a = LI()
d = [-1]*n
d[0] = 0
for i in range(n):
	for j in range(i,min(i+k+1,n)):
		if d[j] == -1:
			d[j] = d[i]+abs(a[i]-a[j])
		else:
			d[j] = min(d[j],d[i]+abs(a[i]-a[j]))
print(d[-1])