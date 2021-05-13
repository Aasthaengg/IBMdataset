n=int(input())
s=input()
ans=0
for i in range(n-1):
    l=set(s[:i+1])
    r=set(s[i+1:])
    pos=l&r
    ans=max(len(pos),ans)
print(ans)