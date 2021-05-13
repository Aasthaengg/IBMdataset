def i():
	return int(input())
def i2():
	return map(int,input().split())
def s():
	return str(input())
def l():
	return list(input())
def intl():
	return list(int(k) for k in input().split())

s = s()
cnt = 0
tmp = ""
word = ""
for i in s:
	word += i
	if tmp != word:
		cnt += 1
		tmp = word
		word = ""
print(cnt)