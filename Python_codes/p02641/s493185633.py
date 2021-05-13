X,N=map(int,input().split())
alist = list(map(int, input().split()))
for a in range(X+1):
    for b in [-1,+1]:
        c = X + a * b
        if alist.count(c) == 0:
            print(c)
            exit(0)