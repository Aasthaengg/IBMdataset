s = input()
k = len(s)

res = 15 - k

must = 8 - res

win = s.count("o")

if win < must:
	print("NO")
else:
	print("YES")