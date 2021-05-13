s = input() + '@'

lst = [1]*len(s)
for i in range(1,len(s)):
  if s[i] == s[i-1]:
    lst[i] = lst[i-1] + 1

ans = 0
for i in range(0,len(s)):
	if s[i] == 'R':
		ans = max(ans,lst[i])

print(ans)

