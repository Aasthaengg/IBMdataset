n, k = input().split()
s = list(input())
n = int(n)
k = int(k)

s[k-1] = chr(ord(s[k-1]) - ord('A') + ord('a'))
for c in s:
	print(c, end="")