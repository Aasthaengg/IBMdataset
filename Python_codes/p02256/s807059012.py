import sys

def gcd(a,b):
	temp = a
	if a<b:
		a=b
		b=temp
	if b==0:
		return a
	c = a%b
	return gcd(b,c)


line = sys.stdin.readline().strip().split(" ")
A = int(line[0])
B = int(line[1])

print(gcd(A,B))