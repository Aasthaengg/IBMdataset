N,x = map(int,input().split())
a = list(map(int,input().split()))
A = sorted(a)

cont = 0
if x > sum(A):
    print(N-1)
else:
    for i in range(N):
        if x >= A[i]:
            x -= A[i]
            cont += 1
    print(cont)