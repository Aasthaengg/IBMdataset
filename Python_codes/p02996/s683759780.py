def solve():
	n = int(input())
	tasks = []
	for i in range(n):
		a, b = map(int,input().split())
		tasks.append((b,a))

	tasks.sort()

	t = 0
	for task in tasks:
		t += task[1]
		if t > task[0]:
			return False
	return True

print("Yes" if solve() else "No")