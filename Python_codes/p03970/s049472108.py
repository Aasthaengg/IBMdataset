r = ['C','O','D','E','F','E','S','T','I','V','A','L','2','0','1','6']
s = list(input())
ans = 0

for i in range(len(s)):
    if s[i] != r[i]:
        ans += 1

print(ans)