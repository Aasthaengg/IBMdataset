import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N=int(input())
    A=list(map(int,input().split()))
    A.append(0)
    len =0
    previous=0

    for i in range(N+1):
        len += abs(A[i] - previous)
        previous =A[i]


    previous =0
    for i in range(N):
        print(len -abs(A[i]-previous)-abs(A[i+1]-A[i])+abs(A[i+1] -previous))
        previous =A[i]







if __name__ == "__main__":
    main()
