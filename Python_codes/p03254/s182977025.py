
N, x = map(int, input().split())
A = [int(i) for i in input().split()]

A.sort()
ans = []
for i in A:
	x -= i
	#print(ans, x)
	if x >= 0:
		ans.append(i)
	else:
		break
	
if x > 0:
	print(len(ans)-1)
else:
	print(len(ans))