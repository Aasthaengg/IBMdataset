H,W,A,B = map(int,input().split())
for j in range(H):
    if j < B:
        for i in range(W):
            if i < A:
                print(0,end="")
            else:
                print(1,end="")
        print()
    else:
        for i in range(W):
            if i < A:
                print(1,end="")
            else:
                print(0,end="")
        print()