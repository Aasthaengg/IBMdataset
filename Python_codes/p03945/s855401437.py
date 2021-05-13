import sys
input=sys.stdin.readline
s=input().rstrip()
t=s[0]
ans=0
for i in range(1,len(s)):
    if s[i]!=t:
        t=s[i]
        ans+=1
print(ans)