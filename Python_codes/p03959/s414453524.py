N=int(raw_input())
T=map(int,raw_input().split())
A=map(int,raw_input().split())

I,J=N-1,0
ans=1
for i in range(N):
    H=min(T[i],A[i])
    if i>0 and T[i-1]<T[i]:
        H=1
        if i+1 <N  and A[i+1]<A[i]:
            if T[i]!=A[i]:
                ans=0
                break
        if i==N-1 and T[i]!=A[i]:
            ans=0
            break
        if T[i] > A[i]:
            ans=0
            break
    if i+1 <N and A[i+1] <A[i]:
        H=1
        if i==0 and T[i]!=A[i]:
            ans=0
            break
        if A[i] > T[i]:
            ans=0
            break
    if i==0:
        H=1
        if T[i] > A[i]:
            ans =0
            break
    if i==N-1:
        H=1
        if A[i] > T[i]:
            ans = 0
            break
    ans *= H
    ans %= 1000000007
print ans

        

