s = list(input())
K = int(input())
zp1 = 1+ord('z')
for i in range(len(s)):
    si = s[i]
    cost = (zp1-ord(si))%26
    if cost <= K:
        K -= cost
        s[i] = 'a'
s[-1] = chr(ord('a') + (K + ord(s[-1]) - ord('a')) % 26)
print(''.join(s))
