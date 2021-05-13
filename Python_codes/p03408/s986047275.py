n = int(input())
slist = [input() for _ in range(n)]
sset = set(slist)
m = int(input())
tlist = [input() for _ in range(m)]

ans = 0
for s in sset:
	if slist.count(s)>tlist.count(s):
		ans =max(ans,slist.count(s)-tlist.count(s))
print(ans)