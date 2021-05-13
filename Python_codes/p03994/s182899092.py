s = input()
k = int(input())

for i in range(len(s)):
    if s[i] != "a":
        req = ord("z") - ord(s[i]) + 1

        if req <= k:
            k -= req
            s = s[:i] + "a" + s[i+1:]

if k > 0:
    s = s[:-1] + chr(ord(s[-1]) + k%26)

print(s)