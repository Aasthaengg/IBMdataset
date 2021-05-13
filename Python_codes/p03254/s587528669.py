N,x = map(int,input().split())
A = list(map(int,input().split()))

if sum(A) < x:
    print(N-1)
else:
    A.sort()
    count = 0
    while(x > 0):
        x -= A[count]
        if x >= 0:
            count += 1
    print(count)