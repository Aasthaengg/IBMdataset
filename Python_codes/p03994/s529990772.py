s = list(input())
K = int(input())
n = len(s)
for i in range(n-1):
    m = ord('z') - ord(s[i]) + 1
    if not s[i] == 'a' and m <= K:
        s[i] = 'a'
        K -= m
s[n-1] = chr((ord(s[n-1])+K%26-97)%26+97)
print(''.join(s))