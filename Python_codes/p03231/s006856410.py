import sys
input = sys.stdin.readline
enum = enumerate
INF = 1001001001

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().rstrip().split()))

def vinput(rep=1, ty=int, cvt=list):
	return cvt(ty(input().rstrip()) for _ in "*"*rep)

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def main():
	N,M = linput()
	S,T = vinput(2,str)
	
	g = gcd(N,M)
	l = lcm(N,M)
	
	res = 0
	if S[::N//g]==T[::M//g]:
		#print(S[::N//g])
		#print(T[::M//g])
		res = l
	else:
		res = -1
	
	#sT = "No Yes".split()
	#print(sT[res])
	print(res)


if __name__ == "__main__":
	main()
