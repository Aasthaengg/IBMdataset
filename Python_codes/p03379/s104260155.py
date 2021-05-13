n = int(input())
X = list(map(int, input().split()))

x = list(enumerate(X))

x.sort(key=lambda x: x[1])
A = list(map(lambda x: x[1], x[n//2-1:n//2+1]))

for v in X:
    if v <= A[0]:
        print(A[1])
    else:
        print(A[0])
