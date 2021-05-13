s = input().strip()
K = int(input())
if K>len(s)*26:
    d = (K-len(s)*26)//26
    K = K-26*d
x = ""
for i in range(len(s)):
    if i<len(s)-1 and (26-(ord(s[i])-ord("a")))%26 <= K:
        x += "a"
        K -= (26-(ord(s[i])-ord("a")))%26
    elif i<len(s)-1:
        x += s[i]
    elif i==len(s)-1:
        k = ord(s[i])+K%26
        if k<=122:
            x += chr(k)
        else:
            x += chr(k-26)
print(x)