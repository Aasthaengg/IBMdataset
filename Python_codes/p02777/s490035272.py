s, t = [i for i in input().split()]
a, b = [int(i) for i in input().split()]
u = input()
if u == s:
	a -= 1
else:
	b -= 1
print("%d %d" % (a, b))