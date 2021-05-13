n = int(input())
aa, bb = [i for i in input().split()]
ret = ''
for a, b in zip(aa, bb):
	ret = ret + a + b
print(ret)