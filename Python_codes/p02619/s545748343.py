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
	D = int(input())  # days
	vC = [0,]+linput()     # decrine rate
	
	#sumC = sum(vC)
	
	# satis (d,i)
	mS = [[0,]+linput() for _ in [0,]*D]
	
	## sample output
	vT = [int(input()) for _ in [0,]*D] ## for p.B

	vL = [-1,]*(26+1)   # last day of Type
	
	#day = -1
	res = 0      # manzoku
	vR = []
	rapp = vR.append
	
	for d in range(D): #[0,364] day
		t = vT[d] ## sample output
		vS = mS[d]
		Sdt = vS[t]
		res += Sdt
		
		vL[t] = d
		C = sum(c*(d-l) for c,l in zip(vC,vL))
		res -= C
		
		rapp(res)
	
	
	#sT = "No Yes".split()
	#print(sT[res])
	#print(res)
	print(*vR, sep='\n')

if __name__ == "__main__":
	main()
