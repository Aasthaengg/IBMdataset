import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    zogen = 0

    ans = 0
    for a, b in zip(A, A[1:]):
        if zogen > 0 and b >= a:
            continue
        if zogen < 0 and b <= a:
            continue
        if zogen == 0:
            zogen = b - a
            continue
        ans += 1
        zogen = 0

    print(ans + 1)



    
    

if __name__ == '__main__':
    main()

