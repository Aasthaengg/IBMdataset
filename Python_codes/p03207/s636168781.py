def resolve():
    N = int(input())
    P = []
    for i in range(N):
        P.append(int(input()))
    total = sum(P)
    maxi = max(P)
    print(total - maxi + maxi//2)
    

if '__main__' == __name__:
    resolve()