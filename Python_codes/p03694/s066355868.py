def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[-1] - A[0])



if '__main__' == __name__:
    resolve()