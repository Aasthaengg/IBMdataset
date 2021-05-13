n, l = map(int, input().split())
s = n * (l-1) + n * (n+1) // 2
i = 1 - l
if i > n:
	i = n
elif i < 1:
  	i = 1
print(s - (l + i - 1))