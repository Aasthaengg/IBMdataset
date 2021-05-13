N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
"""
10       9       8          0+10+9
10   7   9   6   8   5      +9+8+8
10 4 7 3 9 2 6 1 8 0 5 -1   +7+7+6+6  +5+5
                            +4+4+3+3+2+2+1+1+..."""
ans=A[0]

if N>=3:
    ans+=A[1]
if N>=4:
    ans+=A[1]
if N>=5:
    ans+=A[2]
if N>=6:
    ans+=A[2]
if N>=7:
    if N%2:
        ans+=sum(A[3:3+(N+1-6)//2])*2
        ans-=A[3+(N-6)//2]
    else:
        ans+=sum(A[3:3+(N-6)//2])*2
print(ans)