#n=int(input())
#a,b,c=map(int,input().split())
#t=int(input())
#al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
s=list(input())
k=int(input())

if s.count("1")==len(s):
    ans="1"
else:
    for i in range(len(s)):
        if s[i]!= "1":
            break
    if k>i:
        ans=s[i]
    else:
        ans=s[i-1]
print(ans)