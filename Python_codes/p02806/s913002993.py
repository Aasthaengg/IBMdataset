n = int(input())
s = [input().split() for i in range(n)]
x = input()
ind = 0
ans = 0

for i in range(n):
	if s[i][0] == x:
		ind = i

for j in range(ind+1,n):
	ans += int(s[j][1])

print(ans)