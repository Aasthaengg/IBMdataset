s = input()
K = int(input())
alp = 'abcdefghijklmnopqrstuvwxyz'

ans = ''
for i,w in enumerate(s):
    if i != len(s)-1 and (26-(ord(w)-ord('a')))%26 <= K:
        ans += 'a'
        K -= (26-(ord(w)-ord('a')))%26
    elif i != len(s)-1:
        ans += w
    if i == len(s)-1:
        #ans = ans[:-1]
        lastlidx = (ord(w)-ord('a') + K%26)%26
        ans += alp[lastlidx]
print(ans)

