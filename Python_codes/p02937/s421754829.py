s=input()
t=input()
s*=2
next=[[-1]*26 for _ in range(len(s))]
alph=[[]for _ in range(26)]
for i in range(len(s)):
	alph[ord(s[i])-ord("a")].append(i)
from bisect import bisect_right
for i in range(len(s)//2):
	for j in range(26):
		if len(alph[j])>bisect_right(alph[j],i):
			next[i][j]=alph[j][bisect_right(alph[j],i)]
ans=1
now=len(s)//2-1
for x in t:
	r=ord(x)-ord("a")
	now=next[now][r]
	if now==-1:
		print(-1)
		exit()
	if now>=len(s)//2:
		ans+=len(s)//2
		now-=len(s)//2
print(ans+now-len(s)//2)