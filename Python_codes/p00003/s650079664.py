def IsRightTriangle(tri):
	tri.sort()
	return tri[0]**2 + tri[1]**2 == tri[2]**2

N = eval(input())
for i in range(N):
	tri = [eval(item) for item in input().split()]
	print('YES' if IsRightTriangle(tri) else 'NO')