N,A,B=map(int,input().split())

if N==1:
    print(1*(A==B))
else:
    if A>B:
        print(0)
    else:
        print((N-2)*(B-A)+1)
