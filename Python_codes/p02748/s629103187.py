a,b,m = map(int,input().split())
alist = list(map(int,input().split()))
blist = list(map(int,input().split()))
mlist = [list(map(int,input().split())) for s in range(m)]
ans = []
for m in mlist:
	tmp = alist[m[0]-1] + blist[m[1]-1] -m[2]
	ans.append(tmp)
x = min(alist) + min(blist)
ans.append(x)
print(min(ans))