from bisect import bisect_left,bisect_right
N=int(input())
A=list(map(int, input().split()))
A.sort()
ans=0
for i in range(N):
    for j in range(i+1,N):
        a,b=A[i],A[j]
        B=A[j+1:]
        l=abs(a-b)
        r=a+b
        # print(bisect_left(B,r)-bisect_right(B,l))
        ans+=bisect_left(B,r)-bisect_right(B,l)
print(ans)