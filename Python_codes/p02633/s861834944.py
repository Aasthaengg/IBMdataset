x = int(input())
ans = 1
theta = x

while theta != 0:
	ans += 1
	theta = (theta + x) % 360
	
print(ans)