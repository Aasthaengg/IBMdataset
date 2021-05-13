a, b, c = map(int, input().split())

def YesOrNo(a, b, c):
	if a < b < c :
		return "Yes"
	else :
		return "No"

print(YesOrNo(a, b, c))