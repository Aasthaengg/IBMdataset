M, K = map(int, input().split())

if M==1:
    if K==0:
        print(0, 0, 1, 1)
    else:
        print(-1)
    
    exit()

if K>2**M-1:
    print(-1)
    exit()

l = [i for i in range(2**M) if i!=K]
print(*(list(reversed(l))+[K]+l+[K]))