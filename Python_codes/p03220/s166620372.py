import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    lc= 10**6

    for i in range(N):
        c = T - H[i] * 0.006
        if abs(A-c)<lc:
            lc=abs(A-c)
            n= i

    print(n+1)




if __name__ == "__main__":
    main()
