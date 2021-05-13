N,K = map(int,input().split())

H = sorted(map(int,input().split()))

if K >= N:
    print(0)
else:
    print(sum(H[:N-K]))