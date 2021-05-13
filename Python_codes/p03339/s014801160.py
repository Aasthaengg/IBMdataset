import bisect
n = int(input())
s = input()
elist = []
wlist = []
for i in range(n):
	if s[i] == "E":
		elist.append(i)
	elif s[i] == "W":
		wlist.append(i)
ans = 10**18
lenelist = len(elist)
"""
西にいるWを数える
東にいるEを数える
"""
for i in range(n):
	tmp = lenelist-bisect.bisect_right(elist, i)+bisect.bisect_left(wlist, i)
	ans = min(tmp, ans)
print(ans)