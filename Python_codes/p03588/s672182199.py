n = int(input())
a_max = 0
b = -1

for _ in range(n):
	ta,tb = map(int, input().split())
	if ta > a_max:
		a_max = ta
		b = tb

print(a_max + b)