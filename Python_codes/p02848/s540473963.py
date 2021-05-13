n = int(input())
s = input()

ret = ""
for c in s:
	temp = ord(c) + n
	if (temp > 90): temp -= 26
	ret += chr(temp)

print(ret)
