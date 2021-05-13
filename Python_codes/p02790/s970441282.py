m, n = input().split()
str1 = m
str2 = n
if str1 * int(n) < str2 * int(m):
	print(str1 * int(n))
elif str1 * int(n) == str2 * int(m):
	print(str1 * int(n))  
else:
	print(str2 * int(m))
