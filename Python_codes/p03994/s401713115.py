s = list(input())
k = int(input())

for i, c in enumerate(s):
    t = (ord("z") - ord(c) + 1) % 26
    if k >= t:
        s[i] = "a"
        k -= t

t = k % 26
s[-1] = chr(ord(s[-1]) + t)

print("".join(s))