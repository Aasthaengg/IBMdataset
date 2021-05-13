def f(a):
	r = [a[0]*a[2], a[0]*a[3], a[1]*a[2], a[1]*a[3]]
	return max(r)


arr = list(map(int, input().split()))

print(f(arr))