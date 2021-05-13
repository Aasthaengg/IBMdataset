def cross_section_diagram():
	down = []
	edge = []
	pool = []

	for i, c in enumerate(input()):
		if c == '\\':
			down.append(i)
		elif c == '/' and down:
			left = down.pop()
			area = i - left

			while edge:
				if edge[-1] < left:
					break
				edge.pop()
				area += pool.pop()

			edge.append(left)
			pool.append(area)

	print(sum(pool))
	print(len(pool), *pool)

if __name__ == '__main__':
	cross_section_diagram()