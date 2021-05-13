s = list(input())
k = int(input())
n = len(s)
for i in range(n):
    if k <= 0 or s[i] == 'a':
        continue
    if 123 - ord(s[i]) <= k:
        k -= 123 - ord(s[i])
        s[i] = 'a'
# print(k)
# print(s)
k %= 26
# print(ord(s[-1])+k)
if ord(s[-1])+k > 122:
    s[-1] = chr(97+(122-ord(s[-1])+k))
else:
    s[-1] = chr(ord(s[-1])+k)
# print(k)
print(*s, sep='')
