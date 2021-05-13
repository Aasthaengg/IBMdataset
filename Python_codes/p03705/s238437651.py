N,A,B=map(int,input().split())

if A<B:
    if N>2:
        ans=(B-A)*(N-2)+1
    elif N==2:
        ans=1
    else:
        ans=0
elif A==B:
    if N>=1:
        ans=1
    else:
        ans=0
else:
    ans=0

print(ans)