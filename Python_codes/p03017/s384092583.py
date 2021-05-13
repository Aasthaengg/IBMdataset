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
	n,a,b,c,d = linput()
	S = "_" + input().rstrip()
	
	res = 1
	#if c<d:
	X = S[a:c].count("##")
	X += S[b:d].count("##")
	if X!=0: res=0
	
	if c>d:
		Y = S[b-1:d+2].count("...")
		if Y==0: res=0
	
	sT = "No Yes".split()
	print(sT[res])

if __name__ == "__main__":
	main()
