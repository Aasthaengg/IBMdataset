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

flag = 0
if s[0] == "A":
	flag += 1 
cnt1 = 0
for i in range(2,len(s)-1):
	if s[i] == "C":
		cnt1 += 1
if cnt1 == 1:
	flag += 1
cnt2 = 0
for i in range(1,len(s)):
	if s[i].islower():
		cnt2 += 1
if cnt2 >= len(s) -2:
	flag += 1

if flag == 3:
	print("AC")
else:
	print("WA")