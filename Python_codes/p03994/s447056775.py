s=input()
k=int(input())
n=len(s)
ans=""
for i in range(n):
    if i<n-1:
        if s[i]=="a":
            ans+="a"
        else:
            t=123-ord(s[i])
            if k>=t:
                ans+="a"
                k-=t
            else:
                ans+=s[i]
    if i==n-1:
        tt=(ord(s[i])-97+k)%26
        ans+=chr(tt+97)
print(ans)                