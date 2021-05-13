import sys
import os
if sys.platform=="darwin":
	base = os.path.dirname(os.path.abspath(__file__))
	name = os.path.normpath(os.path.join(base, '../Documents/input.txt'))
	#print(name)
	sys.stdin = open(name)

n = int(input())
l = list(map(int,input().split()))

i = 0
ans = 0

while i < n:
	if i==0:
		i = i + 1
	if l[i]==l[i-1]:
		l[i]=max(l)+1
		i = i + 1
		ans = ans + 1
	else:
		i = i + 1

print(ans)
#print(l)


