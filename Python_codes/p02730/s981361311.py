s = input()
n = len(s)
front = (n-1) // 2
rear = (n+2) // 2
sf = s[:front]
sr = s[rear:]
srev = s[::-1]
sfrev = sf[::-1]
srrev = sr[::-1]
if sfrev == sf and srrev == sr and srev == s:
    print('Yes')
else:
    print('No')