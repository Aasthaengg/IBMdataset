n = int(input())
s1 = input()
s2 = input()
i = 0
ans = 1 
while i < len(s1):
	if s1[i] == s2[i] and i == 0:
		ans = 3
		i += 1
		continue
	if s1[i] != s2[i] and i == 0:
		ans = 6
		i += 2
		continue
	if s1[i] != s2[i] and i >= 1 and s1[i-1] == s2[i-1]:
		ans = (ans*2)%(pow(10,9) + 7)
		i += 2
		continue
	if s1[i] != s2[i] and i >= 1 and s1[i-1] != s2[i-1]:
		ans = (ans*3)%(pow(10,9) + 7)
		i += 2
		continue
	if s1[i] == s2[i] and i >= 1 and s1[i-1] != s2[i-1]:
		i += 1
		continue
	if s1[i] == s2[i] and i >= 1 and s1[i-1] == s2[i-1]:
		ans = (ans*2)%(pow(10,9) + 7)
		i += 1
print(ans)