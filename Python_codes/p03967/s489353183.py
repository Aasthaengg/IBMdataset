S = list(input())
g = S.count("g")
p = S.count("p")

s = len(S)

if s % 2 == 0:
	print(int(s // 2) - p)
else:
	print(int((s - 1) // 2) - p)
