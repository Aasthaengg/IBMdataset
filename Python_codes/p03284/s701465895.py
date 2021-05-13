def resolve():
    N, K = map(int, input().split(" "))
    print(1 if N % K != 0 else 0)

if '__main__' == __name__:
    resolve()