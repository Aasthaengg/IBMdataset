n = int(input())
a = list(map(int,input().split()))

print(2*n-1)

if abs(max(a))<abs(min(a)):
	x = a.index(min(a))
	for i in range(n):
		print(x+1,"",i+1)
	for i in range(n-1):
		print(n-i,"",n-i-1)
else:
	x =a. index(max(a))
	for i in range(n):
		print(x+1,"",i+1)
	for i in range(n-1):
		print(i+1,"",i+2)
