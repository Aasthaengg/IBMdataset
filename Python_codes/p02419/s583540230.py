#coding:utf-8

target = input().lower()
ans = 0

while True:
	ss = input()
	if ss == "END_OF_TEXT":
		break
	ans += len([x for x in ss.lower().split() if x == target])

print(ans)