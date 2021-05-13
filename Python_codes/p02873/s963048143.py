from collections import defaultdict

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

def TS(n):
	return n*(n+1)//2

s = input()
l = []
t = [0,0]
b = s[0]
if b=="<":
	a = 0
else:
	a = 1

i=0
while 1:
	if i>len(s)-1:
		l.append(t)
		break
	else:
		if b==s[i]:
			t[a]+=1
			i+=1
		elif s[i]==">":
			a=1
			b = ">"
		else:
			b = "<"
			a=0
			l.append(t)
			t = [0,0]

#print(l)

ans = 0

for i in l:
	ans += TS(i[0]-1)
	ans += TS(i[1]-1)
	ans += max(i)

print(ans)