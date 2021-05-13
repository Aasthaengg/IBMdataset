A,B,C,K=map(int,input().split())
if A>=K:
    print(1*K)
else:
    if A+B>=K:
        print(A)
    else:
        print(A-1*(K-A-B))