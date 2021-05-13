N = int(input())
A = list(map(int,input().split()))

X = sum(A)
Y = 0
MIN = 10**18
for i,a in enumerate(A):
    if i < N-1:
        X -= a
        Y += a
        tmp = abs(X-Y)
        if tmp < MIN:
            MIN = tmp
    
print(MIN)