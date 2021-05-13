import math
n = int(input())
a = list(map(int,input().split()))

b = [0]*n 
s = [0]*(n+1)

for i in reversed(range(1,n+1)):
	for k in range(1,math.floor(n/i)+1):
		j = int(k*i)
		s[i] += b[j-1]
	if s[i]%2 != a[i-1]:
		b[i-1] += 1

L = [i+1 for i in range(n) if b[i] == 1]
print(len(L))
print(*L)