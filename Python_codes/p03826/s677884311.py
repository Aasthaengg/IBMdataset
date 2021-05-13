def judge(A,B,C,D):
    S1 = A*B
    S2 = C*D
    if S1>=S2:
        print(S1)
    else:
        print(S2)

A,B,C,D = map(int,input().split())
judge(A,B,C,D)