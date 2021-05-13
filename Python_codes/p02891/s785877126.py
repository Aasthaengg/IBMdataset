s=input()
k=int(input())

def count_change(st):
    st=st+'!'
    cnt=0
    moji=st[0]
    l=0
    r=0
    for i in range(1,len(st)):
        if moji!=st[i]:
            cnt+=(r-l+1)//2
            l=i
            r=i
            moji=st[i]
        else:
            r=i

    return cnt

if len(set(s))==1:
    ans=len(s)*k//2
    print(ans)
    exit()

if s[0]==s[-1]:
    a=1
    for i in range(len(s)):
        if s[i]!=s[i+1]:
            break
        else:
            a+=1
    
    b=1
    for i in range(len(s)-1,0,-1):
        if s[i]!=s[i-1]:
            break
        else:
            b+=1
    
    ans=count_change(s)*k-(a//2+b//2-(a+b)//2)*(k-1)

else:
    ans=count_change(s)*k

print(ans)