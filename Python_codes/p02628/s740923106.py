M,N = map(int,input().split(" "))
A = list(map(int,input().rstrip().split(" ")))
a=sorted(A)
ans=0
for i in range(N):
    ans+=a[i]
print(ans)