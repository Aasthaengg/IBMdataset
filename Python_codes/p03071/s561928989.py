def resolve():
    A, B = list(map(int,input().split()))
    if A == B:
        print(2*A)
    else:
        print(max(A, B)*2-1)
    

if '__main__' == __name__:
    resolve()