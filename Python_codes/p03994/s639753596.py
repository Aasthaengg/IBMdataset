s = list(input())
k = int(input())
cnt = 0
ans = ''
for i in range(len(s)):
    cnt = (ord('z') - ord(s[i]) + 1) % 26
    if cnt <= k:
        k -= cnt
        s[i] = 'a'
s[-1] = chr((ord(s[-1]) - ord('a') + k) % 26 + ord('a'))
print(*s, sep='')
