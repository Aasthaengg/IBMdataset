A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

v = V - W
if v <= 0:
	print("NO")
else:
	if abs(A - B) <= T * v:
		print("YES")
	else:
		print("NO")
