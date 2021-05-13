A = sorted(list(map(int,input().split())))
cnt = 0
n = (A[2]-A[0])//2
cnt += n
A[0] += 2*n
n = (A[2]-A[1])//2
cnt += n
A[1] += 2*n
A = sorted(A)
if A[0]<A[1]==A[2]:
    cnt += 2
elif A[0]==A[1]<A[2]:
    cnt += 1
print(cnt)