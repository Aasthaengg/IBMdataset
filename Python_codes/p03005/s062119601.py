N, K = map(int,input().split())

min = 1
max = N -(K-1)
if K == 1:
    print(0)
else:
    print(max-min)