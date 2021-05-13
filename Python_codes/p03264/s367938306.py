
def resolve():
    K = int(input())
    a = K//2
    b = K//2 if K%2!=1 else (K//2)+1
    print(a*b)

        

if '__main__' == __name__:
    resolve()