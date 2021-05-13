s = list(input())
l = ['C','O','D','E','F','E','S','T','I','V','A','L','2','0','1','6']
c = 0

for i in range(len(s)):
    if s[i] != l[i]:
        s[i] = l[i]
        c = c + 1

print(c)