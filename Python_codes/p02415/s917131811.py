#coding:utf-8

s=input()
ans = ""
for x in s:
	if x.isupper():
		ans+=x.lower()
	else:
		ans+=x.upper()

print(ans)