n,x = map(int,input().split())
A = list(map(int,input().split()))
B = A.copy()
B = B[::-1]
ans = 0
tmp = 0
for i in range(n-1):
    if A[i] + A[i+1] >x:
        d = (A[i] + A[i+1]) -x
        tmp+= d
        if A[i+1] >=d:
            A[i+1] -=d
        else:
            A[i] = A[i] - (d-A[i+1])
            A[i+1] = 0
A = B
ans = tmp
tmp=0
for i in range(n-1):
    if A[i] + A[i+1] >x:
        d = (A[i] + A[i+1])-x
        tmp+= d
        if A[i+1] >=d:
            A[i+1] -=d
        else:
            A[i] = A[i] - (d-A[i+1])
            A[i+1] = 0

print(min(ans,tmp))
