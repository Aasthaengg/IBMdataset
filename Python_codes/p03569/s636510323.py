s=list(input())

ch=[]
for i in range(len(s)):
    if s[i]!='x':
        ch.append(s[i])

if len(ch)==0:
    print(0)
    exit()
for i in range(len(ch)//2):
    if ch[i]!=ch[len(ch)-i-1]:
        print(-1)
        exit()

ans=0
li=0
ri=0
for i in range(len(ch)//2+1):
    x=0
    while s[li]!=ch[i]:
        x += 1
        li += 1
    li += 1
    y=0
    while s[len(s)-1-ri]!=ch[len(ch)-1-i]:
        y += 1
        ri += 1
    ri += 1
    ans += abs(x-y)

print(ans)