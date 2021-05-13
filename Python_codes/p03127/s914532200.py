n = int(raw_input())
ais = map(int, raw_input().split())
def gcd(a,b):
	return gcd(b, a % b ) if b else a
print reduce(gcd, ais)