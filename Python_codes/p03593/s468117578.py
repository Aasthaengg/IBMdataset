h,w=map(int,input().split())
cnt=[0]*26
for i in range(h):
	a=input()
	for j in range(w):
		cnt[ord(a[j])-ord("a")]+=1
if h%2==1 and w%2==1:
	f=0
	for i in range(26):
		if cnt[i]%2==1:
			cnt[i]-=1
			break
	four=0
	for i in range(26):
		if cnt[i]>=4:
			four+=cnt[i]//4*4
		elif cnt[i]%2==1:
			f=-1
			break
	if four>=h*w-(h//2+w//2)*2-1 and f==0:
		f=1
	else:
		f=0
elif h%2==0 and w%2==0:
	f=1
	for i in range(26):
		if cnt[i]%4!=0:
			f=0
			break
else:
	if h%2==0:
		h,w=w,h
	two=0;f=0
	for i in range(26):
		if cnt[i]%4==2:
			two+=2
		elif cnt[i]%2==1:
			f=-1
			break
	if two<=w and f==0:
		f=1
	else:
		f=0
print("Yes" if f else "No")