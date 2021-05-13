N = int(input())
A = list(map(int, input().split()))

h = 0
r = 0
for v in A:
	need = 0 if v >= h else h-v
	r += need
	h = need + v
print(r)
