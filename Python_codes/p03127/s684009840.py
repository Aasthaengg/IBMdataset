import sys
input = sys.stdin.readline
def gdc(p, q):
    if q == 0:
        return p
    return gdc(q, p%q)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(A[0])
        return
    res = A[0]
    for i in range(1,N):
        res = gdc(res, A[i])
    print(res)

if __name__ == '__main__':
    main()