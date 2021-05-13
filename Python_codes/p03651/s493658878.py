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

def bye(res):
	sT = "IMPOSSIBLE POSSIBLE".split()
	print(sT[res])
	#print(res)
	exit(0)

def main():
	N,K = linput()
	vA = linput(int,set)

	res = 0
	l,r = min(vA), max(vA)
	if K in vA:
		bye(1)
	if not K<=r:
		bye(0)

	g = 0	# GCD for all
	for a in vA:
		g = gcd(g, a)
	print(g, file=sys.stderr)###
	
	if (r-K)%g:
		res = 0
	else:
		res = 1
	bye(res)


if __name__ == "__main__":
	main()
