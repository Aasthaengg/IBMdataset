n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_tot = sum(a)

for i in range(n):
	a[i], b[i] = a[i] - b[i], b[i] - a[i]
	if b[i] > 0:
		a[i+1] -= b[i]
	if a[i] < 0:
		a[i] = 0
	if a[i+1]<0:
		a[i+1] = 0
print(a_tot-sum(a))