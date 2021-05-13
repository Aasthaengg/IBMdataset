n,m = map(int,input().split())
lr= [list(map(int,input().split()))for a in range(m)]
l,r = [list(b) for b in zip(*lr)]
left,right = max(l),min(r)
cnt = 0
for i in range(1,n+1):
	if left <= i and i <= right:
		cnt += 1
print(cnt)