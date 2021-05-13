import collections
s,t = raw_input().split(' ')

a,b = map(int,raw_input().split(' '))
u = raw_input()
if u == s:
	a -=1
elif u == t:
	b -=1
print '{} {}'.format(a,b)