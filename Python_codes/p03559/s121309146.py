import bisect
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
for b in B:
    ia = min(bisect.bisect_left(A,b),N-1)
    ic = min(bisect.bisect_right(C,b),N-1)
    a = ia if A[ia]>=b else ia+1
    c = N-ic-1 if C[ic]<=b else N-ic
    ans += a*c
print(ans)