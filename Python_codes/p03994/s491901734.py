s = list(input())
k = int(input())
n = len(s)
for i in range(n):
    if s[i]=='a':continue
    d = ord('z')-ord(s[i])+1
    if d<=k:
        s[i] = 'a'
        k -= d

x = (ord(s[-1])-ord('a')+k)%26
s[-1] = chr(ord('a')+x)

print(''.join(s))
