import sys
input = sys.stdin.readline
enum = enumerate

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def vinput(rep=1, ty=int, cvt=list):
	return cvt(ty(input().rstrip()) for _ in "*"*rep)

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def main():
	N = int(input())
	vA = linput()
	vA.sort()
	vA.reverse()
	
	res = 0
	res = sum(vA[1:2*N+1:2])
	#sT = "No Yes".split()
	#print(sT[res])
	print(res)

if __name__ == "__main__":
	main()
