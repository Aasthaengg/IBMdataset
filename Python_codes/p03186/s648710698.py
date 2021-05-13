a, b, c = map(int, input().split())
cnt = 0

if c <= a + b + 1:
	cnt = b + c
else:
	cnt = a + b + 1 + b

print(cnt)