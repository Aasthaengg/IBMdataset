s=list(input())
n=len(s)
ans=0
for i in range(2**(n-1)):
    a=list(bin(i)[2:])
    a=['0']*(n-1-len(a))+a
    j=0
    num=s[0]
    while j<n-1:
        if a[j]!='0':
            ans += int(num)
            num=''
        j+=1
        num+=s[j]
    ans+=int(num)
print(ans)