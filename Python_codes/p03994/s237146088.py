s = list(input())
n = len(s)
k = int(input())
t = [ord(s[i]) - 97 for i in range(n)]
for i in range(n):
    if k == 0:
        break
    x = 26 - t[i]
    if 0 < x % 26 <= k:
        k -= x
        s[i] = "a"
t[-1] = ord(s[-1]) - 97
if k > 0:
    s[-1] = chr((k + t[-1]) % 26 + 97)
print("".join(s))