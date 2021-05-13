num = int(raw_input())
x = raw_input().split()
i = 0
y = []
while i < num :
	y.append(int(x[i]))
	i = i + 1
ma, mi = y[0], y[0]
i = 1
while i < num :
	if ma < y[i] :
		ma = y[i]
	if mi > y[i] :
		mi = y[i]
	i = i + 1
s = sum(y)
print u"%d %d %d" % (mi, ma, s)