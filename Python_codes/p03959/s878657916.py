n=int(input())
s=list(map(int, input().split()))
t=list(map(int, input().split()))
ans=1
if s[s.index(max(s))]!=t[s.index(max(s))]:ans=0
t=t[::-1]
a=[1]+[0]*(n-2)+[1]
for i in range(1,n-1):
    if s[i]<a[i-1]:
        ans=0
        break
    elif s[i]>s[i-1]:a[i]=1
    else:a[i]=s[i-1]
for i in range(1,n-1):
    if t[i]<t[i-1]:
        ans=0
        break
    elif t[i]>t[i-1]:a[n-i-1]=1
    else:a[n-i-1]=min(t[i-1],a[-1*(i+1)])
for i in a:
    ans=(ans*i)%(10**9+7)
print(ans)