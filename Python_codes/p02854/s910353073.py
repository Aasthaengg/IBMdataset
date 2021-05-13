n = int(input())
a = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(a[i]+s[i])
m = 100000000000000
for i in range(len(s)):
	m = min(m, abs((s[i] - s[0]) - (s[len(s) - 1] - s[i])))
print(m)