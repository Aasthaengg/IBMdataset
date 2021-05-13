H,N,*A = map(int, open(0).read().split())
if sum(A) >= H:
    print('Yes')
else:
    print('No')