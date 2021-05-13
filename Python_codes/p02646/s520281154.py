x = input().split()
a, v = int(x[0]), int(x[1])
x = input().split()
b, w = int(x[0]), int(x[1])
t = int(input())
if abs(b-a)+w*t <= v*t:
	print("YES")
else:
	print("NO")