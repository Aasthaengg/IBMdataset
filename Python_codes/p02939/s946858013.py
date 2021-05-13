from collections import defaultdict
 
def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()
 
s = readChar()
if len(s)==1:
	print(1)
	exit()
b="-1"
ans=0
l = [""]
while len(s)>1:
	if l[-1]!=s[:1]:
		l.append(s[:1])
		s = s[1:]
	else:
		l.append(s[:2])
		s = s[2:]
if s!="":
	l.append(s)
del l[0]

#print(l)
if l[-1]==l[-2]:
	del l[-1]

print(len(l))