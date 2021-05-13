import sys
input=sys.stdin.readline
s=input().rstrip()
ans=1000
for i in range(26):
    x=chr(97+i)
    temp=0
    pre=list(s)
    while True:
        check=True
        for j in pre:
            if j!=x:
                check=False
        if check:
            ans=min(ans,temp)
            break
        temp+=1

        post=[]
        for j in range(len(pre)-1):
            if pre[j]==x or pre[j+1]==x:
                post.append(x)
            else:
                post.append('!')
        pre=post

print(ans)