s = list(str(input()))
k = int(input())
for i in range(len(s)):
    if s[i] != "a":
        num = 26-(ord(s[i])-ord("a"))
        if k >= num:
            k -= num
            s[i] = "a"
s[-1] = chr(ord("a")+((ord(s[i])-ord("a")+k)%26))
print("".join(s))