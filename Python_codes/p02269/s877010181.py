n = int(input())
S = {}

ans = []
for i in range(n):
	order = input().split()
	if order[0] == "insert":
		S[order[1]] = 0
	elif order[0] == "find":
		if order[1] in S:
			ans.append("yes")
		else:
			ans.append("no")

for i in range(len(ans)):
	print(ans[i])
