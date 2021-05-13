N = int(input())
A = list(map(int,input().split()))
isMinus = False
for i in range(N):
    if A[i] < 0:
        isMinus = not isMinus
        A[i] = A[i]*-1

if isMinus:
    print(sum(A)-min(A)*2)
else:
    print(sum(A))
