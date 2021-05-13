N,x = map(int,input().split())
A = sorted(list(map(int,input().split())))
if x>=2*sum(A):
    print(0)
else:
    ind = N
    for i in range(N):
        x -= A[i]
        if x<0:
            ind = i
            break
    if ind==N and x>0:
        A = sorted(A,reverse=True)
        for i in range(N):
            x -= A[i]
            if x<0:
                ind -= 1
                break
    print(ind)