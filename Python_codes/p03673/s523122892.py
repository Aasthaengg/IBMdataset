import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N % 2 == 0:
        B = A[1::2]
        B.reverse()
        B += A[0::2]
    else:
        B = A[0::2]
        B.reverse()
        B += A[1::2]
    print(" ".join(map(str, B)))


if __name__ == "__main__":
    main()
