def resolve():
    N, K = list(map(int, input().split()))
    print(len(list(filter(lambda x: x >= K, map(int, input().split())))))

if '__main__' == __name__:
    resolve()