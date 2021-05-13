s=input()
k=int(input())
n=len(s)
num=[0]*n
for i in range(n):
    if s[i]!="a":
        num[i]=123-ord(s[i])
if sum(num)>=k:
    ans=""
    for i in range(n-1):
        if k>=num[i]:
            k-=num[i]
            ans+="a"
        else:
            ans+=s[i]
    if k>=num[-1]:
        ans+="a"
    else:
        ans+=chr(97+((ord(s[-1])-97+k)%26))
else:
    k-=sum(num)
    ans="a"*(n-1)
    ans+=chr(97+(k%26))
print(ans)
