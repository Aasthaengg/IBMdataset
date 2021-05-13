from collections import Counter
C=Counter()

h,w=map(int,input().split())
for _ in range(h):
	C+=Counter(input())

one=[]
two=[]
four=[]
twolim=(h//2)*(w%2)+(w//2)*(h%2)
twocnt=0
for k,v in C.items():
	while v>=4:
		v-=4
		four.append(k)
	if v>=2:
		twocnt+=1
		if twocnt>twolim:
			print("No")
			exit()
		two.append(k)
	if v%2:
		if one or h%2==w%2==0:
			print("No")
			exit()
		one.append(k)
print("Yes")		
		
"""
ans=[""]*h

for i in range(h//2):
	c=0
	while c<w//2:
		c+=1
		x=four.pop()
		ans[i]+=x
		ans[~i]+=x
	if w%2:
		if two:
			x=two.pop()
			ans[i]+=x
			ans[~i]+=x
		else:
			x=four.pop()
			ans[i]+=x
			ans[~i]+=x
			four.append(x)
if h%2:
	for x in two+four+four+one:
		ans[h//2]+=x
for l in ans:
	print(l+l[:w//2][::-1])
"""