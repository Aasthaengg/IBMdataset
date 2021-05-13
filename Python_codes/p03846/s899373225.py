n = int(input())
a = list(map(int,input().split()))

mod = 10**9 + 7

lis = [0] * n

for i in a: lis[i] += 1

for i in range(1,n):
	if lis[i] % 2 == 1:
		print(0)
		exit()
		
print(pow(2, n//2, mod))
