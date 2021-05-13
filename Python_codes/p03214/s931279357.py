n=int(input())
A=list(map(int,input().split()))
mu=sum(A)/n
diff=1000
ans=0
for i,a in enumerate(A):
    if abs(a-mu)<diff:
        diff=abs(a-mu)
        ans=i
print(ans)