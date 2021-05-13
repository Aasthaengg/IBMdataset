n=int(input())
s=list(str(input()))
s.sort()
cnt=2
ans=1
for i in range(n-1):
    if s[i]==s[i+1]:
        cnt+=1
    else:
        ans*=cnt
        cnt=2
ans*=cnt
print((ans-1)%(10**9+7))