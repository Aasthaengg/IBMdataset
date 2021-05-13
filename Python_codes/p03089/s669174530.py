n = int(input())
a = list(map(int,input().split()))

def solve(l,ans):
	if l == []:
		return ans
	for i in range(len(l)-1,-1,-1):
		if l[i] == i+1:
			ans.append(i+1)
			return solve(l[:i]+l[i+1:], ans)

	return 0


A = solve(a,[])
if A == 0:
	print(-1)
else:
	for a in A[::-1]:
		print(a)