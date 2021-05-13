n,k=map(int,input().split())
h=[int(input()) for _ in range(n)]
h_sort=sorted(h)
a=0
b=10**20
for i in range(k, n+1):
	a=h_sort[i-1] - h_sort[i-k]
	if a<b:
		b=a
print(b)