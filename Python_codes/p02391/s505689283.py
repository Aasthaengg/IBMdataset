a, b = map(int, input().split())

def BorS(a, b):
	if a == b : return "a == b"
	if a > b : return "a > b"
	if a < b : return "a < b"

print(BorS(a, b))