a, b = (int(x) for x in input().split())
if a > b:
	answer = "a > b"
elif a == b:
	answer = "a == b"
else:
	answer = "a < b"
print(answer)

