def resolve():
    N, D = list(map(int, input().split()))
    print(N//(2*D+1) if N%(2*D+1)==0 else (N//(2*D+1))+1)
    
if '__main__' == __name__:
    resolve()