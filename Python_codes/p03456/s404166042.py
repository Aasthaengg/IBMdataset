import math
def issquare(res):
	ans = math.sqrt(res)
	return (ans - math.floor(math.sqrt(res))) == 0

a, b = map(str, input().split())
t = a + b
res = int(t)
ans = issquare(res)
if ans:
	print("Yes")
else:
	print("No")