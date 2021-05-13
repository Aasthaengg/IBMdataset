n=int(input())
s=input()
t="ABC"
c=0
for i in range(n-2):
	if s[i]==t[0] and s[i+1]==t[1] and s[i+2]==t[2] :
		c+=1
print(c)