import sys
s = input()
res = 0
for x in s:
	if (x == '+'): res += 1
	else: res -= 1
print (res)