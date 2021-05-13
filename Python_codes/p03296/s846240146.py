import sys
input = sys.stdin.readline

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def main():
	n=int(input())
	vA=linput()
	
	res = 0
	pp = 0
	
	for a in vA:
		if pp==a:
			res += 1
			pp = 0
		else:
			pp = a
	
	#sT = "No Yes".split()
	#print(sT[res])
	print(res)

if __name__ == "__main__":
	main()
