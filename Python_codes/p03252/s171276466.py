from sys import exit

s=input()
t=input()
alp=[0]*26
for i in range(len(s)):
	if alp[ord(s[i])-97]==0:
		alp[ord(s[i])-97]=t[i]
	else:
		if alp[ord(s[i])-97]!=t[i]:
			print("No")
			exit()
			
alp=[0]*26
for i in range(len(t)):
	if alp[ord(t[i])-97]==0:
		alp[ord(t[i])-97]=s[i]
	else:
		if alp[ord(t[i])-97]!=s[i]:
			print("No")
			exit()

print("Yes")