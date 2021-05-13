import sys
input = sys.stdin.readline

def linput():
	return list(map(float,input().split()))

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def main():
	S = input().rstrip()
	
	res = 0
	B = 0
	
	for s in S:
		if s=='B': B+=1
		else: res += B
	print(res)

if __name__ == "__main__":
	main()
