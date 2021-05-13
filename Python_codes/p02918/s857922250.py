n,k = map(int,input().split())
s = input()

cnt = 0
for i in range(len(s)):
	if s[i] == 'L':
		if i == 0:
			continue
		if s[i-1] == 'L' :
			cnt += 1
	else:
		if i == len(s) - 1:
			continue
		if s[i+1] == 'R' :
			cnt += 1

print(min(n-1,cnt + k*2))