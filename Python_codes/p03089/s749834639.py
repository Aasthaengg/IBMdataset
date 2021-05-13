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
	N, = linput()
	vB = linput()
	
	vC = [b-i-1 for i,b in enum(vB)]
	vC.reverse()
	#print(N)
	res = 0
	vR = []
	
	for _ in "*"*N:
		try:
			x = vC.index(0)
			vR.append(vB[N-x-1])
			vC[x] = -INF
			for j in range(x):
				vC[j] += 1
		except ValueError as e:
			print(-1)
			return
	
	#sT = "No Yes".split()
	#print(sT[res])
	#print(res)
	print(*vR[::-1], sep="\n")

if __name__ == "__main__":
	main()
