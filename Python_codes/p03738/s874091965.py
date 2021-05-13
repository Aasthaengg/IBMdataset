import sys
input = sys.stdin.readline


def read():
    A = input().strip()
    B = input().strip()
    return A, B


def solve(A, B):
    if len(A) > len(B):
        return "GREATER"
    elif len(B) > len(A):
        return "LESS"
    else:
        for i in range(len(A)):
            if int(A[i]) > int(B[i]):
                return "GREATER"
            elif int(B[i]) > int(A[i]):
                return "LESS"
    return "EQUAL"


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
