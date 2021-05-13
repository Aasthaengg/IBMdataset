s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

flg = False
for i in range(len(s)):
    if i >= len(t):
        break
    if ord(s[i]) > ord(t[i]):
        break
    if ord(s[i]) < ord(t[i]):
        flg = True
        break
    if i == len(s)-1 and i < len(t)-1:
        flg = True
        break
        
print('Yes') if flg else print('No')