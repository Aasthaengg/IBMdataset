k=int(input())
s=input()

if len(s)<=k:
    print(s)
else :
    ans=str()
    for i in range(k):
        ans+=s[i]
    print(ans+'...')
