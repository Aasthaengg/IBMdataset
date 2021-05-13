s = input()
temp = 10**9
x = []
y = []
for i in range(len(s)):
	if s[i] =="A":
		x.append(i)
	elif s[i]=="Z":
		y.append(i)

mx = min(x)
mz = max(y)


print((mz-mx)+1)