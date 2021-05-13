s = list(input())
k = int(input())
for i in range(len(s)):
    if s[i] == "a":
        continue
    c = ord(s[i]) - ord("a")
    if k >= (26 - c):
        k -= 26 - c
        s[i] = "a"
s[-1] = chr(((ord(s[-1]) - ord("a")) + k) % 26 + ord("a"))
print("".join(s))
