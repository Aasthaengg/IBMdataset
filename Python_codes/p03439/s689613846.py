from sys import stdout,exit
n = int(input())
print(0)
stdout.flush()
a = input()
if a=="Vacant": exit()
else: l = 0
print(n-1)
stdout.flush()
b = input()
if b=="Vacant": exit()
else: r = n-1
while True:
	m = (l+r)//2
	print(m)
	stdout.flush()
	c = input()
	if c=="Vacant": break
	elif (a!=c)^((m-l)%2): r = m
	else: l,a = m,c
exit()