s=input()
ans = "Good"
for i in range(1,len(s)):
	if s[i]==s[i-1]:ans = "Bad"
print(ans)
