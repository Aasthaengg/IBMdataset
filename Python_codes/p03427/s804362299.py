import sys
input = sys.stdin.readline

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def dist(x1,y1,x2,y2):
	return abs(x1-x2)+abs(y1-y2)

def main():
	#N = int(input())
	S = input().rstrip()
	
	res = 0
	l,r = 0,0
	for s in S:
		d = int(s)
		l += 9 if r else d-1
		r += d
	
	res = max(l,r)
	print(res)
	#sT = "No Yes".split()
	#print(sT[res])
	

if __name__ == "__main__":
	main()
