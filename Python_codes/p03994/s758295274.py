s = list(input())
K = int(input())
l = len(s)
for i in range(l-1):
    x = (ord('a')-ord(s[i])) % 26
    if x <= K:
        K -= x
        s[i] = 'a'
s[l-1] = chr(ord('a') + (ord(s[-1])-ord('a')+K) % 26)
print(''.join(s))