s = input()
k = int(input())
result = ""
i = 0
#a:97, z:122
while i < len(s)-1:
    s_i = ord(s[i])
    if s[i]=="a":
        result = result+"a"
    elif 123-s_i <= k:
        result = result+"a"
        k -= 123-s_i
    else:
        result = result+s[i]
    i += 1
if k>0:
    result = result + chr((ord(s[i])-97+k)%26+97)
else:
    result = result + s[i]

print(result)