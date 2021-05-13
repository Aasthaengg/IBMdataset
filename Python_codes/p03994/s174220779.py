s = list(input())
k = int(input())
for i in range(len(s)):
    if s[i] != "a" and (123-ord(s[i])) <= k:
        k -= (123-ord(s[i]))
        s[i] = "a"
    if i == len(s)-1:
        s[i] = (chr((((ord(s[i])+(k%26))-97)%26)+97))
print("".join(s))