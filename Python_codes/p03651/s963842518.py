import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

gcd = A[0]

if N == 1:
	if K == A[0]:
		print('POSSIBLE')
		exit()
	else:
		print('IMPOSSIBLE')
		exit()

for i in range (0, N):
	if gcd > 1:
		gcd = math.gcd(gcd, A[i])
	else:
		break
        
if gcd == 1:
	print('POSSIBLE')
elif K%gcd ==0 and K <= max(A):
	print('POSSIBLE')
else:
	print('IMPOSSIBLE')