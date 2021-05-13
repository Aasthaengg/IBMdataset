import sys
input = sys.stdin.readline

# C - When I hit my pocket...
def get_max_biscuits():
	
	if K < A + 1:
		return K + 1
	else:
		count = K - (A+1)
		
		return B + (B-A)*(count//2) + count%2


K, A, B = map(int, input().split())

if B - A >= 2:
	print(get_max_biscuits())
else:
	print(K + 1)