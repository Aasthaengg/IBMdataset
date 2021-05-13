a, b = map(int, input().split())

# 両辺の偶奇に着目
# 両辺の偶奇が異なれば等号が成立しない
if a % 2 != b % 2:
	print('IMPOSSIBLE')
else:
  	print(int((a + b) / 2))