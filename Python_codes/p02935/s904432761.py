def resolve():
    N = int(input())
    V = list(map(int, input().split()))
    import itertools
    ans = 0
    for i in range(N-1):
        V = sorted(V, reverse=True)
        v1 = V.pop()
        v2 = V.pop()
        V.append((v1+v2)/2)
    print(V[0])
    


    
if '__main__' == __name__:
    resolve()