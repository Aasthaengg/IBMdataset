n = int(input())
s = input()
x=0
ans =0
for i in range(0,n):
	if s[i]=='I':
		x =x+1
		ans = max(ans, x)
	else:
		ans = max(ans, x)
		x = x-1
print(ans)