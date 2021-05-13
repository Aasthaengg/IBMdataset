n  =int(input())
s = input()
x = 0
c = 0
x1 = 0
t = []
for i in s:
	if i=='I':
		c+=1
	if c>x:
		x =c
	elif i=='D':
		c-=1
	if c>x1:
		x1=c

	t.append(max(x1,x))
print(max(t))
