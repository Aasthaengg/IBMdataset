s = list(input())
k = int(input())
n = len(s)
alph_map = {chr(ord('a') + i): (26 - i) % 26 for i in range(26)}
for i in range(n):
    if k >= alph_map[s[i]]:
        k -= alph_map[s[i]]
        s[i] = 'a'
if k > 0:
    s[n-1] = chr((ord(s[n-1]) + k % 26) % 123)
print(''.join(s))
