import sys

sys.setrecursionlimit(10 ** 9)


# map(int, sys.stdin.read().split())


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    B = list(map(int,input().split()))
    B.append(10**6)
    A =[]
    A.append(B[0])
    for i in range(N-1):
        a =min(B[i],B[i+1])
        A.append(a)
    print(sum(A))




if __name__ == "__main__":
    main()
