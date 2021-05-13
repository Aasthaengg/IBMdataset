s=input()
k=int(input())
num=[(123-ord(s[i]))%26 for i in range(len(s))]
ans=""
for i in range(len(s)-1):
    if num[i]<=k:
        ans+="a"
        k-=num[i]
    else:
        ans+=s[i]
k%=26
if num[-1]<=k:
    ans+=chr(97+k-num[-1])
else:
    ans+=chr(ord(s[-1])+k)
print(ans)
