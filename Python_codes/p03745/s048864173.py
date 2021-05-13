import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def solve(N, A):
    B = [A[0]]
    prev = A[0]
    for a in A:
        if prev != a:
            B.append(a)
            prev = a
    count = 1
    up = False
    down = False
    for i in range(1, len(B)):
        if not up and not down:
            if B[i-1] < B[i]:
                up = True
            else:
                down = True
        elif up and B[i-1] > B[i]:
            up = False
            count += 1
        elif down and B[i-1] < B[i]:
            down = False
            count += 1
    return count


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
