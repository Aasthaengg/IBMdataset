s=input().lower()
cnt=0
while True:
	r=input()
	if r=='END_OF_TEXT': break
	cnt+=r.lower().split().count(s)
print(cnt)