import sys
input = sys.stdin.readline

# B - RGB Boxes
R, G, B, N = map(int, input().split())
ans = 0

for r in range(N + 1):
	for g in range(N + 1):
		b_sum = N - R*r - G*g
		
		if b_sum < 0:
			break
		else:
			if (b_sum / B).is_integer():
				ans += 1

print(ans)

