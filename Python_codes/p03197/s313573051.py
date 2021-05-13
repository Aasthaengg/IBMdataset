n=int(input())
a=[int(input())for _ in range(n)]
f=1
for i in range(n):
	if a[i]%2==1:
		f=0
		break
print("second" if f else "first")