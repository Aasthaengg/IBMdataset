import sys
import os
if sys.platform=="darwin":
	base = os.path.dirname(os.path.abspath(__file__))
	name = os.path.normpath(os.path.join(base, '../Documents/input.txt'))
	#print(name)
	sys.stdin = open(name)

n = int(input())
l = input()

#print(l)
lsh = []*(n+1)
lsh.append(0)
sharp = 0
comma = 0

for i in range(n):
	if l[i]=="#":
		sharp = sharp + 1
	lsh.append(sharp)
#print(lsh)

for i in range(n-1,-1,-1):
	#print(i)
	if l[i]==".":
		comma = comma + 1
	lsh[i] = lsh[i] + comma

print(min(lsh))


