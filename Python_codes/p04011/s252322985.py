
def resolve():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())
    xdays = min(N, K)
    ydays = max(N-K, 0)
    print(X*xdays+Y*ydays)
    
    


if '__main__' == __name__:
    resolve()