n = int(input())
l = list(map(int, input().split()))

Max = l[0]
for i in range(n):
	if Max < l[i]:
		Max = l[i]
		
l.remove(Max)
s = sum(l)
if Max < s:
	print('Yes')
else:
	print('No')