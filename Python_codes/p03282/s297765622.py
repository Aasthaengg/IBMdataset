s=input()
k=int(input())
for i in range(len(s)):
	if s[i]!="1":
		print(s[i])
		exit()
	elif i==k-1:
		print(1)
		exit()