import sys
input = sys.stdin.readline

N,X=map(int,input().split())
vA=list(map(int,input().split()))
vA.sort()

res=0
for a in vA:
	if a<=X:
		res += 1
		X -= a
	else:
		break
else:
	if X:
		res = max(0, res-1)

print(res)
