n = int(input())
s = input()

tmp = 0
for i in range(n-1):
	for j in range(i+tmp+1, n):
		if not s[i:j] in s[j:]:
			break
	tmp = max(tmp, j-i-1)

"""
二重ループ型だが実際はO(ans N)でうごく.
"""

print(tmp)