n = int(input())
b = list(map(int,input().split()))
b.append(100000+1)
a = [b[0]]
for i in range(n-1):
	if b[i] > b[i+1]:
		b[i] = b[i+1]
	a.append(b[i])
print(sum(a))