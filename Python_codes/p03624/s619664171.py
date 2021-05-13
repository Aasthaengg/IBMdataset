Sset=set(input())
Sset=sorted(Sset)

ans = "None"
flg = True
last = "None"
for i,c in enumerate(Sset):
	if i+97 !=ord(c):
		flg=False
		ans = chr(i+97)
		break
	last = c

if flg and last != 'z' :
	ans = chr(ord(last)+1)
print(ans)
