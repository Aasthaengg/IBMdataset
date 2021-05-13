import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N=int(input())
    A=list(map(int,input().split()))
    AS =sorted(A)
    right = AS[N//2]
    left = AS[N//2 -1]
    for a in A:
        if a<=left:
            print(right)
        else:
            print(left)




if __name__ == "__main__":
    main()
