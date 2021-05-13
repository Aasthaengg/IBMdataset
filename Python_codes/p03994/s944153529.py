s = input()
k = int(input())

res=[]
for i in range(len(s)):
    num = ord(s[i])-97

    if i==len(s)-1:
        res.append(chr((num+k)%26+97))
    elif s[i] == "a":
        res.append("a")
    elif 26 - num <= k:
        res.append("a")
        k-=26-num
    else:
        res.append(s[i])

print("".join(res))