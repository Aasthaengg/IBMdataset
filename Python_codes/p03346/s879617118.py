N = int(input())

lis = [0] * (N+1)

for i in range(N):

    P = int(input())

    lis[P] = lis[P-1] + 1

print (N - max(lis))
