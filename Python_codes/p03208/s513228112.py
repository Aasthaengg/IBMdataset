import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())


    H=[]
    for i in range(N):
        H.append(int(input()))

    H.sort()
    mm = 10**9+7
    for i in range(N-K+1):
        mm=min(mm,H[i+K-1] -H[i] )

    print(mm)


if __name__ == "__main__":
    main()
