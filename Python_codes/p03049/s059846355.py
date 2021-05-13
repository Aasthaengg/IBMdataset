N=int(input())
a=0
b=0
ab=0
ans=0
for _ in range(N):
    s=input()
    ans+=s.count('AB')
    if s[0]=='B' and s[-1]=='A':
        ab+=1
    elif s[0]=='B':
        b+=1
    elif s[-1]=='A':
        a+=1
if ab==0:
    print(ans+min(a,b))
else:
    if a==0 and b==0:
        print(ans+ab-1)
    else:
        print(ans+min(a+ab,b+ab))
