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
	vRan = [chr(i+ord("a")) for i in range(26)]
	random.shuffle(vRan)
	sr = "".join(vRan)
	print(sr)
	return sr

def main():
	S = input().rstrip()
	#S = ran()###
	#vS = [input().rstrip() for _ in [0,]*N]
	N = len(S)
	oA = ord("a")
	vD = [chr(i+oA) for i in range(26)]
	#vD += [".","#"]

	for d in vD:
		if d not in S:
			print(S+d)
			return
	
	if S=="".join(vD[::-1]):
		print(-1)
		return

	vQ = []
	vR = [ord(s) for s in S]
	vQ.append(vR.pop())
	
	while vR:
		r = vR.pop()
		nowq = INF
		for q in vQ:
			if q>r:
				nowq = min(nowq,q)
		if nowq<INF:
			vR.append(nowq)
			break
		vQ.append(r)
	
	res = "".join(chr(r) for r in vR)
	print(res)
	#sT = "No Yes".split()
	#print(sT[res])
	

if __name__ == "__main__":
	main()
