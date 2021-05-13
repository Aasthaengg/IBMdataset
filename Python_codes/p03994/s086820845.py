alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = input()
K = int(input())
ans = ''
for i in range(len(s) - 1):
    s_i = alphabet.index(s[i])
    if s[i] == 'a':
        ans += 'a'
        continue
    if (26 - s_i <= K):
        K -= 26 - s_i
        ans += 'a'
    else:
        ans += s[i]
ans += alphabet[(K + alphabet.index(s[-1])) % 26]
print(ans)
