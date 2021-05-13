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
	N = int(input())
	vAB = [linput() for _ in [0,]*N]

	res = 0
	for a,b in reversed(vAB):
		c = (a+res)%b
		if c:
			res += b-c
	
	print(res)
	#sT = "No Yes".split()
	#print(sT[res])
	

if __name__ == "__main__":
	main()
