s=input()
n=len(s)
i,a,ans=0,0,0
while i<n:
    if s[i]=="A":
        a+=1
        i+=1
    elif i<n-1 and s[i:i+2]=="BC":
        ans+=a
        i+=2
        while i<n:
            if s[i]=="A":
                a+=1
                i+=1
            elif i<n-1 and s[i:i+2]=="BC":
                ans+=a
                i+=2
            else:
                a=0
                i+=1
                break
    else:
        i+=1
        a=0
print(ans)