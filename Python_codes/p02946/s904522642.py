def resolve():
    K, X = list(map(int, input().split()))
    print(*list(range(-1000000, 1000001, 1))[X-K+1000000+1:X+K+1000000])

if '__main__' == __name__:
    resolve()