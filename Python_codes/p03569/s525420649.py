s=input()
left=0
right=len(s)-1
ans=0
while left<right:
    if s[left]==s[right]:
        left+=1
        right-=1
    elif s[left]=="x":
        left+=1
        ans+=1
    elif s[right]=="x":
        right-=1
        ans+=1
    else:
        print(-1)
        exit()
print(ans)