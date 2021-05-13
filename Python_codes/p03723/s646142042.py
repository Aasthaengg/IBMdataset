def resolve():
    A,B,C = map(int,input().split())
    count = 0
    if A == C and A == B:
        if A % 2 == 1:
            print(0)
        else:
            print(-1)
    else:
        while (A % 2 == 0 and B % 2 == 0 and C % 2 == 0):
            tmpA = (B + C) / 2 
            tmpB = (A + C) / 2 
            tmpC = (A + B) / 2
            A = tmpA
            B = tmpB
            C = tmpC
            count = count + 1
        print(count)
resolve()