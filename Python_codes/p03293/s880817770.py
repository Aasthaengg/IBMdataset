s = input()
t = input()

res = False
for _ in range(len(s)):
    if s == t:
        res = True
        break
    s = s[1:] + s[0]
print('Yes' if res else 'No')
