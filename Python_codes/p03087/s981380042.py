import bisect
n,q = map(int,input().split())
s = input()
acindex = []
for i in range(n-1):
	if s[i]=="A" and s[i+1]=="C":
		acindex.append(i+1)
for _ in range(q):
	l,r = map(int,input().split())
	count = bisect.bisect_left(acindex, r)-bisect.bisect_left(acindex, l)
	print(count)