import bisect

n,c,k = list(map(int, input().split()))
t = []
for i in range(n):
	t.append(int(input()))
t.sort()

ans = 0
remain = c-1
if c==1:
	print(n)
	exit()
time = t[0]
for i in range(1,len(t)):
	if time+k<t[i]:
		time = t[i]
		remain = c
		ans+=1
	if remain==0:
		remain=c
		time = t[i]
		ans+=1
	remain-=1

print(ans+1)