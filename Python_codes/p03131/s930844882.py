K,A,B = map(int,input().split())

if B-A < 3:
    print(K+1)
else:
    if A > K-1:
        print(K+1)
    else:
        count = K-A+1
        shou = count//2
        if count%2 == 1:
            print(A+(B-A)*shou+1)
        else:
            print(A+(B-A)*shou)