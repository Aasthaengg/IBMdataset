def resolve():

    A,B,C=map(int,input().split())
    val=A-B
    print(C-val if C-val>=0 else 0)

resolve()