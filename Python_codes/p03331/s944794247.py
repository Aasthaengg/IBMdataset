n=int(input())
ans=10e5
for a in range(1,n//2+1):
    b=n-a
    ans=min(ans,sum([int(i) for i in str(a)])+sum([int(i) for i in str(b)]))
    ans=min(ans,sum([int(i) for i in str(a)])+sum([int(i) for i in str(b)]))
print(int(ans))