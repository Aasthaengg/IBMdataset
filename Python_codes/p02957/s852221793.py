def resolve():
    A, B = list(map(int, input().split()))
    print((A+B)//2 if (A+B)%2==0 else "IMPOSSIBLE")

    
if '__main__' == __name__:
    resolve()