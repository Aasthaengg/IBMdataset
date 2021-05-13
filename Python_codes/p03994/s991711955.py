s = list(input())
k = int(input())
num = len(s)

for i in range(num):
    a = 122-ord(s[i])+1
    if a <= k and s[i] != 'a':
        k -= a
        s[i] = 'a'
if k > 0:
    s[-1] = chr(ord(s[-1])+k%26)
print(*s, sep='')
        
