a=list(map(int,input().split()))
a.sort()
A,B,C=a

ans=0
ans+=C-B

# ans += (C-(A+C-B))/2
ans +=(B-A)//2

if A%2 != B%2:
    ans+=2

print(ans)