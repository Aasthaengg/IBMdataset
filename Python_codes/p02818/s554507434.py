A,B,K = map(int,input().split())

if A+B<=K:
    print("0 0")

else:
    if A>=K:
        print("{} {}".format(A-K,B))
    else :
        
        B = B-(K-A)
        A = 0
        print("{} {}".format(A,B))