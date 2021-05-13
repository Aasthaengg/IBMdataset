s = list(input().split())
a, b = list(map(int, input().split()))
z = input()
k = a - 1
m = b - 1
if s[0] == z:
	print(k, end=' ')
	print(b)
elif s[1] == z:
	print(a, end=' ')
	print(m)