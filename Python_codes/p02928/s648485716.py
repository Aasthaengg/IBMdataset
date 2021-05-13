n,k = map(int,input().split())
A = list(map(int,input().split()))
ans1 = 0
ans2 = 0
for i in range(n):
    l = 0
    for j in range(i+1,n):
        if  A[i] > A[j]:
            l += 1
    ans1 += l
    m = 0
    for j in range(i+1):
        if A[i] > A[j]:
            m += 1
    ans2 += l+m
print((ans1*k+ans2*(k*(k-1)//2))%(10**9+7))