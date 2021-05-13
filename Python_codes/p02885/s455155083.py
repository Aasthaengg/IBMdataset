def resolve():
    A, B = list(map(int, input().split()))
    print(max(A-2*B, 0))
    
if '__main__' == __name__:
    resolve()