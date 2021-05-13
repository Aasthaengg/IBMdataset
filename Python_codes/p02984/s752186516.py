n = int(input())
a = list(map(int,input().split()))
b = [0]*n
sum = 0
for i in range(n):
	sum += pow(-1,i)*a[i]
b[0] = sum//2
for i in range(1,n):
	b[i] = -b[i-1] + a[i-1]
c = [n*2 for n in b]
L=[str(a) for a in c]
L=" ".join(L)
print(L)