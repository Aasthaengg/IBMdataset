def resolve():
    N = int(input())
    K = int(input())
    res = 1
    for i in range(N):
        if res < K:
            res += res
        else:
            res += K
    print(res)

            

if '__main__' == __name__:
    resolve()