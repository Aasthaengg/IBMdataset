K,A,B = map(int, open(0).read().split())
if B - A <= 1:
    print(K+1)
else:
    if K < A + 1:
        print(K+1)
    else:
        dm = divmod(K-A-1,2)
        print((dm[0]*(B-A)+B+dm[1]))