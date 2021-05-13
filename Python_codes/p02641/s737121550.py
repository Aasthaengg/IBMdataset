x,n = map(int, input().split())
if n > 0:
	l = list(map(int,input().split()))
else:
	l = []
tl = []
for i in range(0,102):
	if i not in l:
		tl.append(i)
tlabs = []
for i in tl:
	tlabs.append(abs(x - i))
ans = tl[tlabs.index(min(tlabs))]
print(ans)