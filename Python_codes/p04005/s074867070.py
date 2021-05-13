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
	#n=int(input())
	#vA=linput()
	a,b,c = linput()
	
	res = 0
	
	x = (a%2)*b*c
	y = (b%2)*c*a
	z = (c%2)*a*b
	
	res = min(x,y,z)
	
	#sT = "No Yes".split()
	#print(sT[res])
	print(res)
 
if __name__ == "__main__":
	main()