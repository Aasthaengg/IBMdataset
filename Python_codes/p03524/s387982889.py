S = list(input())

ma = 0
for s in set(S):
	cnt = S.count(s)
	ma = max(ma, cnt)
	
if len(S) - ma >= (ma - 1) * 2 or len(S) == 1:
	print("YES")
else:
	print("NO")