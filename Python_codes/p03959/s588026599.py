N=int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
a = 1
if T[0]>A[0] or A[-1]>T[-1] or T[-1]!=A[0]:
    a*=0
for i in range(1,N-1):
    if T[i-1]!=T[i]:
        if T[i]>A[i]:
            a*=0
            break
        else:
            a*=1
            
    elif A[i]!=A[i+1]:
        if T[i]<A[i]:
            a*=0
            break
        else:
            a*=1
    else:        
        a=(a*min(T[i],A[i]))%(10**9+7)
print(a)