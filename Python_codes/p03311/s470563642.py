n=int(input())
a=list(map(int,input().split()))

A = sorted([a[i] - i for i in range(n)])
b = A[n//2]
ans=0
for i in range(n):
    ans += abs(a[i] - (b+i))
print(ans)