import sys
input = sys.stdin.readline
enum = enumerate
INF = 1001001001

import collections
import random

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def dist(x1,y1,x2,y2):
	return abs(x1-x2)+abs(y1-y2)

def ran():
	vRan = [random.randint(1,5) for i in range(8)]
	return vRan

def main():
	if 1:
		N,M,K = linput()
		vA = linput()
		vB = linput()
	else:
		#vA=[5, 3, 3, 5, 3, 4, 1, 4]
		#vB=[5, 1, 4, 1, 1, 2, 1, 2]
		#4
		N,M,K = 0,0,8
		vA = ran()
		vB = ran()
		print(vA,vB,sep="\n")###
	
	res = 0
	
	cnt = 0
	t = 0
	for a in vA:
		if t+a<=K:
			t += a
			cnt += 1
		else: break
	
	res = max(res,cnt)
	vJ = vA[0:cnt]
	for b in vB:
		while t+b>K:
			if not vJ: break
			j = vJ.pop()
			t -= j
			cnt -= 1
		if t+b<=K:
			t += b
			cnt += 1
			res = max(res,cnt)
		else:
			break
		#print(res,cnt)
	
	print(res)
	#sT = "No Yes".split()
	#print(sT[res])
	

if __name__ == "__main__":
	main()
