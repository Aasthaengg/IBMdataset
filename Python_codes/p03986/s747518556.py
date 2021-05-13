s=input()
n,ans,l=len(s),len(s),0
for c in s:
	if c=='S':
		l += 1
	elif l:
		l -= 1
		ans -= 2
print(ans)
