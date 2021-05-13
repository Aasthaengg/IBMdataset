N,K = map(int,input().split(" "))
if N<K:
    print(1)
else:
    if N%K==0:
        print(0)
    else:
        print(1)