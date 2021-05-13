import sys
input = sys.stdin.readline

# C - XYZ Triplets
def calc(x, y, z):
	return x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x


N = int(input())
ans = [0] * (N + 1)

for x in range(1, 100):
	for y in range(1, 100):
		for z in range(1, 100):
			i = calc(x, y, z)
			
			if i > N:
				break
			else:
				ans[i] += 1

for i in range(1, N + 1):
	print(ans[i])
			
 			   
