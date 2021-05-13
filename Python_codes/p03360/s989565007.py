def resolve():
    A, B, C = list(map(int, input().split(" ")))
    K = int(input())
    m = max(A, B, C)
    mul = m * 2 ** K
    print(sum([A, B, C]) - m + mul)

if '__main__' == __name__:
    resolve()