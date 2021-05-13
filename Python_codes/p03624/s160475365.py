s = input()

b = [True] * 26
for c in s:
    b[ord(c) - ord('a')] = False

ans = 'None'
for i in range(26):
    if b[i]:
        ans = chr(ord('a') + i)
        break
print(ans)
