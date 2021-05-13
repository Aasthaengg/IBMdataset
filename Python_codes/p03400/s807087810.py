

n = int(raw_input())
d,x = map(int, raw_input().split())
ais = [int(raw_input()) for _ in range(n)]

def f(ai,d):
	return 1 + (d-1)/(ai)

print x + sum([f(ai,d) for ai in ais] or [0])