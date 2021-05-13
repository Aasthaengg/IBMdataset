n=int(input())
a=list(map(int, input().split()))
a.sort()

b=0
for i in range(1, 1+n):
	b += a[-(2*i)]
print(b)