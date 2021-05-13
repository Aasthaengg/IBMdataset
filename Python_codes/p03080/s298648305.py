N=int(input())
s=input()
ct=0
for i in range(len(s)):
	if s[i]=='R':
		ct+=1
print("Yes" if 2*ct>len(s) else "No")