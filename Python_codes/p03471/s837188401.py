import sys

input = sys.stdin.readline

N, Y = list(map(int,input().split()))

Aohashi = False
for a in range(N+1):
	for b in range(N+1-a):
		c = N-a-b
		otoshidama = 10000*a+5000*b+1000*c
		if otoshidama==Y:
			Aohashi = True
			break
	if Aohashi: break

if Aohashi:
	print(a,b,c)
else:
	print(-1,-1,-1)