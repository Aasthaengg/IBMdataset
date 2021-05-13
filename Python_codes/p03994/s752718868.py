s=input()
n=len(s)
k=int(input())
ans=[]
for i in range(n):
    if i==n-1:
        ans.append(chr(((ord(s[i])-97+k)%26)+97))
    else:

        if s[i]=="a":
            ans.append("a")
        else:
            if 26-(ord(s[i])-97)<=k:
                ans.append("a")
                k-=(26-(ord(s[i])-97))
            else:
                ans.append(s[i])
print("".join(ans))
