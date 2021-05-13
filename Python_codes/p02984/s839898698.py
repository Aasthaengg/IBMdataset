N = int(input())
*A, = map(int, input().split())

x = 0
for i, a in enumerate(A):
    if i%2==0:
        x += a
    else:
        x -= a


for i in range(N):
    print(x)
    x = 2*A[i]-x
