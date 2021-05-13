n=int(input())

def keta(num):
    s = str(num)
    sm=0
    for i in range(len(s)):
        sm+=int(s[i])
    return sm

ans=10**10
for a in range(1,n):
    b=n-a
    ans=min(ans,keta(a)+keta(b))

print(ans)