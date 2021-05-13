import sys
input=sys.stdin.readline
s=input().rstrip()
idousaki=0
ans=0
for i in range(len(s)):
    if s[i]=="W":
        ans+=(i-idousaki)
        idousaki+=1

print(ans)