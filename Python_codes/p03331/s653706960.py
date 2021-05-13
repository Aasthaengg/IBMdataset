n=int(input())
ans=10e5
for a in range(1,n//2+1):
    b=n-a
    ans=min(ans,sum(map(int,str(a)))+sum(map(int,str(b))))
print(int(ans))
