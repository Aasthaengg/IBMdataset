A, B = map(int, input().split())
if A >= 13:
	B = B
elif A <= 12 and A >= 6:
  B = B // 2
elif A < 6:
  B *= 0
print(B) 