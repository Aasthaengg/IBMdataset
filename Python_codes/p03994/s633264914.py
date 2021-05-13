s = list(input())
K = int(input())
a = ord('z') + 1
for i in range(len(s)-1):
    if s[i] == 'a':
        continue
    #print(K,a - ord(s[i]))
    if K >= (a - ord(s[i])):
        K -= a - ord(s[i])
        s[i] = 'a'
    #print(K,a - ord(s[i]))
i = len(s)-1
s[len(s)-1] = chr((ord(s[i])-ord('a') + K) % 26 + ord('a'))
print(''.join(s))
