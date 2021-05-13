
N = int(input())

A = list(map(int,input().split()))

ans = 3**N

d = 1
for i in range(N):

    if A[i] % 2 == 1:
        d *= 1
    else:
        d *= 2

print (ans - d)
