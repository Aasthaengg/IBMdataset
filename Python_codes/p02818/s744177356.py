def resolve():
    A, B, K = list(map(int, input().split()))
    taka = max(A-K, 0)
    ao = max(B-(K-A), 0) if K > A else B
    print(taka, ao)

if '__main__' == __name__:
    resolve()