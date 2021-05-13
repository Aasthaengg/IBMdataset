alice = 0
bob = 0
n = int(input())
a = list(map(int,input().split()))
sorted_a = sorted(a, reverse=True) 

for i in range(n):
	if i % 2 == 0:
		alice += sorted_a[0]
	else:
		bob += sorted_a[0]
	sorted_a.pop(0)

print(alice - bob)