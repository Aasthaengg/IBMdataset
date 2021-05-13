def koch(n, left, right):
	vector = [(right[0] - left[0])/3, (right[1] - left[1])/3]
	vector_up = [-vector[1]*(3**0.5)/2, vector[0]*(3**0.5)/2]
	point1 = [left[0] + vector[0], left[1] + vector[1]]
	point2 = [left[0] + 2*vector[0], left[1] + 2*vector[1]]
	middle = [left[0] + vector[0]*3/2 + vector_up[0],
			  left[1] + vector[1]*3/2 + vector_up[1]]

	if n == 0:
		return [right]

	if n == 1:
		return [point1, middle, point2, right]

	return koch(n-1, left, point1) + koch(n-1, point1, middle)\
			+ koch(n-1, middle, point2) + koch(n-1, point2, right)

if __name__ == "__main__":
	for point in [[0,0]] + koch(int(input()), [0,0], [100,0]):
		print(*point)
