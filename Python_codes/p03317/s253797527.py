import sys

def resolve():
    N, K = list(map(int, input().split(" ")))
    A = list(map(int, input().split(" ")))
    res = 0
    covered = 0
    while True:
        if covered >= N:
            break
        if res == 0:
            covered = K
        else:
            covered += K - 1
        res += 1
    print(res)

if '__main__' == __name__:
    resolve()