N,M = list(map(int,input().split()))
A = list(map(int,input().split()))

A.sort(reverse=True)

all_ = sum(A)
th = all_/(4*M)

ans='Yes'
if A[M-1] < th:
    ans='No'
    
print(ans)